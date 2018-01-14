% This SPM regressor generation script assumes that there exists a csv file
% with columns specifiying all the info necessary for generate the model.
% These columns must include the labels 'run','regID','onset','duration',
% and, if parametric modulation is desired, 'param'
%
% If this file exists, then this script will read in the file, find the
% appropriate columns, and turn it into .mat files specifying model
% conditions. 

% Contrasts may also be specified. The script will keep track of
% which columns are in the design matrix so that the contrasts will match
% the current design-- even if some conditions are missing in some runs or
% if an arbitrary number of covariates are included in the model (e.g., 
% spike regressors).
%
% Maureen Ritchey, 2011-2016

clear all;
addpath('/Volumes/External/MemoHR/Scripts/helper'); % path to helper files (e.g., initializeVars)

%%% FILE INFORMATION

% modelLabel tells me which csv file gets loaded in to define the regressors - see MemoHR_itemSourceModel_spec.R
modelLabel = 'ItemSourceDM'; 

% other file info
outputDir = '/Volumes/External/MemoHR/Analysis/ItemSourceDM_rf_new/';
datadir = '/Volumes/External/MemoHR/Data/Behavioral/';
funcdir = '/Volumes/External/MemoHR/Data/MRI/';
subjID = {'s04' 's05' 's06' 's07' 's08' 's09' 's10' 's11' 's13' 's14' 's16' 's17' 's18' ...
     's19' 's20' 's21' 's22' 's23' 's25' 's26' 's27' 's28'};

conLabel = '_cons';

write_reg = 1; %do you want to write out regressor mats?
write_con = 1; %do you want to write out contrasts?

%%%DATA INFORMATION

% modeltype: 'block' or 'ER' 
% (ER=durations set to zero, block=durations set to duration value)
modeltype = 'ER'; % actually mixed but duration defined for all

% other trial type info
regnames = {'EmoR-SC' 'EmoR-SI' 'EmoK' 'EmoM' 'NeuR-SC' 'Neu-SI' 'NeuK' 'NeuM' 'Other'};
regids = [1 2 3 4 5 6 7 8]; %values taken on by each trial of interest in regcol
regmax = 8; %max value for a trial of interest

%%% CONTRAST INFORMATION

% include motion regressors in the model? 1 for standard 6-param motion regs, 2 for motion+spikes
inc_motion = 2;
spike_regs = 'strict_spike_regs_rp.txt'; %used only if inc_motion==2
% note that strict_spike_regs includes spike regressors using a relatively
% 'strict' threshold for defining bad timepoints

% specify contrasts according to regID
% for positive only contrasts, simply include one row, e.g., [1 2]
% for subtraction contrasts, include two rows with pos in first row,
% negative in second row, e.g., [1;2]
% if subtraction contrasts are unbalanced (e.g., condition 1 vs 2 & 3), use
% NaN to balance, e.g., [1 NaN; 2 3]
contrasts = {[1 2 3 4 5 6 7 8] [1] [2] [3] [4] [5] [6] [7] [8]...
              [1 2 3 4; 5 6 7 8] [1 5;2 6] [1 2 5 6; 3 4 7 8] ...
              [1;2] [5;6] [1 2; 3 4] [5 6; 7 8] ...
              [1 2; 5 6] [1; 5] [1 2 7 8; 5 6 3 4] [1 6;2 5]};
contrast_names = {'ALL' 'EmoR-SC' 'EmoR-SI' 'EmoK' 'EmoM' 'NeuR-SC' 'NeuR-SI' 'NeuK' 'NeuM' ...
                'EmovNeu' 'R-SCvSI' 'RvKM' ...
                'EmoR-SCvSI' 'NeuR-SCvSI' 'EmoRvKM' 'NeuRvKM' ...
                 'EmovNeu_R' 'EmovNeu_R-SC' 'EmovNeu_RvKM' 'EmovNeu_R-SCvSI'};

%%% PARAMETRIC MODULATION

pmodON = 0; % 1 for parametric modulation (look for params columns), 0 for off

% if pmodON
%         
%     % notes: modulators will be mean-centered within each run. order of the
%     % modulators matters! i.e., the 2nd modulator is actually the effect of
%     % mod 2 accounting for the effects of mod 1. if one modulator has no
%     % variance within a run, then all modulators for that run will be
%     % excluded.
%     
%     pmod_name = {'RecRate' 'SourceRate'}; % cell array of modulator name(s), in order of param columns
%     pmodrange = {[0 1] [0 1]}; %expected range for modulators (will error if exceeded)
%     pmodpoly = {[1] [1]}; %polynomial expansion, 1 for linear
%     regs_w_pmod = {'Emo' 'Neu'}; %regressors with parametric modulators
%     
%     % add parametric contrasts to end
%     % add decimal point for param modulator, e.g., 1.2 for regressor 1, modulator 2 
%     % (note: may need to adjust if using >=10 modulators)
%     contrasts = [contrasts ...
%         [1.1 2.1] [1.1] [2.1] [1.1;2.1] ...
%         [1.2 2.2] [1.2] [2.2] [1.2;2.2]];
%     contrast_names = [contrast_names ...
%         'pALL_rec' 'pEmo_rec' 'pNeu_rec' 'pEmoVNeu_rec' ...
%         'pALL_src' 'pEmo_src' 'pNeu_src' 'pEmoVNeu_src'];
%    
% end

%%%END OF MODIFICATION%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% GET TRIAL INFORMATION %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if ~exist(outputDir)
    mkdir(outputDir);
end
save(strcat(outputDir,'model_info'));

for iSub = 1:length(subjID)
    
    b = initializeVars_MemoHR(subjID,iSub); % get subject specific paths etc
    
    if ~exist(strcat(outputDir,subjID{iSub}))
        mkdir(strcat(outputDir,subjID{iSub}));
    end
    
    datafile = strcat(datadir,subjID{iSub},'/',subjID{iSub},'_',modelLabel,'.csv');
    fprintf('\nReading file %s\n',datafile);
    
    tmpcond = tdfread(datafile,',');
    condfields = fieldnames(tmpcond);
    
    tri.runs = tmpcond.(condfields{find(cellfun(@length,strfind(condfields,'run')))});
    tri.conds = tmpcond.(condfields{find(cellfun(@length,strfind(condfields,'regID')))});
    tri.ons =  tmpcond.(condfields{find(cellfun(@length,strfind(condfields,'onset')))});
    
    % get durations if block design
    if strcmp(modeltype,'block')
        tri.durs =  tmpcond.(condfields{find(cellfun(@length,strfind(condfields,'duration')))});
    elseif strcmp(modeltype,'ER')
        tri.durs = zeros(size(tri.ons,1),1);
    else
        error('Pick a valid model type, block or ER');
    end
    
    % get parametric modulators
    if pmodON
        paramidx = find(cellfun(@length,strfind(condfields,'param'))); % allow for multiple parametric regressors
        if ~isempty(paramidx)
            for p=1:length(paramidx)
                tri.params(p).vals = tmpcond.(condfields{paramidx(p)});
            end
        end
    end
    
    runs = unique(tri.runs);
    % if want to exclude certain runs, add that info here by subsetting
    % runs for particular subjects
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%% GENERATE REGRESSORS %%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    %contrast manager will store which trial types are in which column -
    %essential for setting up contrast vectors correctly
    %note that contrast_man must be the same length as the number of betas
    %in the model minus session means!! otherwise spm_FcUtil error
    contrast_man = [];
    
    %%%Generate regressor files
    for iRun = 1:length(runs)
        curfuncrun = strcat(funcdir,subjID{iSub},'/',b.taskruns{runs(iRun)},'/');
        
        filename = strcat(outputDir,subjID{iSub},'/',modelLabel,'_',subjID{iSub},'_run',num2str(runs(iRun)),'_regs');
        regs = unique(tri.conds(tri.runs==runs(iRun)));
        
        % initialize  variables
        onsets = {}; names = {}; durations = {};
        if pmodON, pmod = struct('name',{},'poly',{},'param',{}); end
        
        % initialize switch for skipping regs in contrast manager
        keep_reg = zeros(length(regs));
        if pmodON, keep_param = zeros(length(regs),length(tri.params)); end
        
        for iReg = 1:length(regs)
            %find trial types of interest
            if regs(iReg) <= regmax
                rowids = find(tri.conds==regs(iReg) & tri.runs==runs(iRun));
            end
            
            %if they exist in this run, add the regressor information
            if rowids
                add_dur = tri.durs(rowids)';
                add_dur(isnan(add_dur))=0;
                onsets = [onsets tri.ons(rowids)'];
                durations = [durations add_dur];
                names = [names regnames{regids==regs(iReg)}];
                keep_reg(iReg) = 1;
                
                % parametric modulation
                if pmodON && sum(strcmp(regs_w_pmod,regnames{regids==regs(iReg)})) % if we're doing pmod for this reg
                    for p = 1:length(tri.params)
                        
                        % get vals, inspect, & mean center
                        vals = tri.params(p).vals(rowids)';
                        if min(vals)<pmodrange{p}(1) || max(vals)>pmodrange{p}(2) % just double checking vals
                            fprintf('On %s, run %d, regressor %d, parameter values not as expected\n',subjID{iSub},iRun,iReg);
                            error('Parametric values not as expected')
                        end
                        vals = vals - mean(vals); % mean-center within run
                        
                        % add in modulator info
                        if length(unique(vals))>1 % include parametric regressor only if more than one value in this run
                            pmod(iReg).poly(p) = pmodpoly(p);
                            pmod(iReg).name(p) = pmod_name(p);
                            pmod(iReg).param(p) = {vals};
                            keep_param(iReg,p) = 1;
                            fprintf('On %s, regressor %d: Including parametric modulator %s, run %d.\n',subjID{iSub},iReg,pmod_name{p},iRun);
                        else
                            warning('On %s, run %d, regressor %d, only one parametric value assigned.\nAll parametric regressors skipped for that run.\n',subjID{iSub},iRun,iReg);
                        end
                    end
                end
            else
                warning('On %s: No trials for %s in %s\n',subjID{iSub},regnames{regids==regs(iReg)},b.taskruns{runs(iRun)})
            end
            
        end %iReg
        
        
        %save a set of regressors for each run
        if write_reg
            fprintf('Run %0.0f: Saving %0.0f regressors to file %s\n',runs(iRun),length(names),filename);
            if pmodON && min(min(keep_param))==1
                save(filename,'names','onsets','durations','pmod');
            else
                save(filename,'names','onsets','durations');
            end
            clear names onsets durations pmod
        end
        
        %regressor columns to contrast manager
        for iReg = 1:length(regs)
            if keep_reg(iReg)
                contrast_man = [contrast_man regids(regids==regs(iReg))];
            end
            if keep_reg(iReg) && pmodON && min(min(keep_param))==1 % if all param modulators intact for that run
                for p = 1:length(tri.params)
                    contrast_man = [contrast_man (p*.1)+regids(regids==regs(iReg))];
                end
            end
        end
        
        %add motion regressor columns to contrast manager if desired
        if inc_motion==1 %pad run with 6 motion parameters
            contrast_man = [contrast_man repmat(regmax+1,1,6)];
        elseif inc_motion==2 %pad run with # columns in spike_regs (or whatever file specified)
            curspikes = strcat(curfuncrun,spike_regs);
            spk = importdata(curspikes);
            spkcols = size(spk,2);
            contrast_man = [contrast_man repmat(regmax+1,1,spkcols)];
        end
        
    end %iRun
    
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%% GENERATE CONTRAST VECTORS %%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    contrast_vectors = {};
    for iCon = 1:length(contrasts)
        curVector = zeros(size(contrast_man));
        curCon = contrasts{iCon};
        
        %find positively- and negatively-weighted columns
        for j=1:size(curCon,2)
            curVector(contrast_man==curCon(1,j)) = 1;
            if(size(curCon,1)>1)
                curVector(contrast_man==curCon(2,j)) = -1;
            end
        end
        
        %scale beta weights to sum to one
        posweight = 1./(size(find(curVector==1),2));
        negweight = -1./(size(find(curVector==-1),2));
        curVector(curVector==1)=posweight;
        curVector(curVector==-1)=negweight;
        
        contrast_vectors = [contrast_vectors curVector];
    end %iCon
    
    %save a single contrast file per subject
    filename = strcat(outputDir,subjID{iSub},'/',modelLabel,'_',subjID{iSub},conLabel);
    if write_con
        fprintf('Saving %0.0f contrasts to file %s\n',length(contrast_names),filename);
        save(filename,'contrast_vectors','contrast_names');
    end
    
end %iSub
