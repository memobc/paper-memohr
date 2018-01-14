function [] = batch()

clear all;
curdir = pwd;
addpath('/Volumes/External/MemoHR/Scripts/helper'); % path to helper files (e.g., initializeVars)

%Specify variables
outLabel = 'ItemSourceDM'; %output label
subjects = {'s04' 's05' 's06' 's07' 's08' 's09' 's10' 's11' 's13' 's14' 's16' 's17' 's18' 's19' 's20' 's21' 's22' 's23' 's25' 's26' 's27' 's28'}; 

analysisDir = '/Volumes/External/MemoHR/Analysis/ItemSourceDM_rf_new/';
analysisName = outLabel;
explicitMask = ''; % no explicit mask
funcFilter = '^rf'; % run on native-space resliced images
cons = '_cons.mat';

do_model = 1;
do_cons = 1;

errorlog = {}; ctr=1;

for i=1:length(subjects)
    cd(curdir);
    
    %Define variables for individual subjects
    b = initializeVars_MemoHR(subjects,i);

    b.analysisDir = strcat(analysisDir,b.curSubj,'/');
    b.analysisName = analysisName;
    b.explicitMask = explicitMask;
    b.funcFilter = funcFilter;
    b.cons = cons;
    b.replace_cons = 0;
    
    if do_model
        
        %specify matlabbatch variable with subject-specific inputs
        matlabbatch = batch_model_template(b);
        
        %save matlabbatch variable for posterity
        outName = strcat(b.analysisDir,outLabel,'_',date);
        save(outName, 'matlabbatch');
        
        %run matlabbatch job
        try
            spm_jobman('initcfg')
            spm('defaults', 'FMRI');
            spm_jobman('serial', matlabbatch);
        catch err
            errorlog{ctr,1} = subjects{i};
            errorlog{ctr,2} = 'model';
            errorlog{ctr,3} = err;
            ctr = ctr + 1;
            cd(scriptdir);
            continue;
        end
        
    end
    
    if do_cons
        batch_contrasts(b);
    end
    
end

if ~isempty(errorlog)
    disp(errorlog) % print error log at end
else
    disp('No errors detected.');
end

end

%%%%BATCH FUNCTIONS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%MODEL FUNCTIONS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [matlabbatch]=batch_model_template(b)
%This function generates the matlabbatch variable: can be copied in
%directly from the batch job output, then modify lines as necessary to
%generalize the paths, etc, using inputs variables
%-----------------------------------------------------------------------
% Job configuration created by cfg_util (rev $Rev: 4252 $)
%-----------------------------------------------------------------------
matlabbatch{1}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{1},'/']};
matlabbatch{1}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{1}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{2}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{2},'/']};
matlabbatch{2}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{2}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{3}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{3},'/']};
matlabbatch{3}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{3}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{4}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{4},'/']};
matlabbatch{4}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{4}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{5}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{5},'/']};
matlabbatch{5}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{5}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{6}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{6},'/']};
matlabbatch{6}.cfg_basicio.file_fplist.filter = b.funcFilter;
matlabbatch{6}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{7}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{1},'/']};
matlabbatch{7}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{7}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{8}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{2},'/']};
matlabbatch{8}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{8}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{9}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{3},'/']};
matlabbatch{9}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{9}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{10}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{4},'/']};
matlabbatch{10}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{10}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{11}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{5},'/']};
matlabbatch{11}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{11}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{12}.cfg_basicio.file_fplist.dir = {[b.dataDir,'/',b.taskruns{6},'/']};
matlabbatch{12}.cfg_basicio.file_fplist.filter = '^strict_spike';
matlabbatch{12}.cfg_basicio.file_fplist.rec = 'FPList';
matlabbatch{13}.spm.stats.fmri_spec.dir = {b.analysisDir};
matlabbatch{13}.spm.stats.fmri_spec.timing.units = 'secs';
matlabbatch{13}.spm.stats.fmri_spec.timing.RT = 2.01;
matlabbatch{13}.spm.stats.fmri_spec.timing.fmri_t = 16;
matlabbatch{13}.spm.stats.fmri_spec.timing.fmri_t0 = 1;
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).src_exbranch = substruct('.','val', '{}',{1}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(1).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(1).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run1_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(1).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).src_exbranch = substruct('.','val', '{}',{7}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(1).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(1).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).src_exbranch = substruct('.','val', '{}',{2}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(2).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(2).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run2_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(2).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).src_exbranch = substruct('.','val', '{}',{8}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(2).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(2).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).src_exbranch = substruct('.','val', '{}',{3}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(3).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(3).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run3_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(3).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).src_exbranch = substruct('.','val', '{}',{9}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(3).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(3).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).src_exbranch = substruct('.','val', '{}',{4}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(4).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(4).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run4_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(4).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).src_exbranch = substruct('.','val', '{}',{10}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(4).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(4).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).src_exbranch = substruct('.','val', '{}',{5}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(5).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(5).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run5_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(5).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).src_exbranch = substruct('.','val', '{}',{11}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(5).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(5).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).tname = 'Scans';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).sname = 'File Selector (Batch Mode): Selected Files (^rf)';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).src_exbranch = substruct('.','val', '{}',{6}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(6).scans(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(6).cond = struct('name', {}, 'onset', {}, 'duration', {}, 'tmod', {}, 'pmod', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi = {[b.analysisDir b.analysisName '_' b.curSubj '_run6_regs.mat']};
matlabbatch{13}.spm.stats.fmri_spec.sess(6).regress = struct('name', {}, 'val', {});
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1) = cfg_dep;
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).tname = 'Multiple regressors';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).tgt_spec{1}(1).name = 'class';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).tgt_spec{1}(1).value = 'cfg_files';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).tgt_spec{1}(2).value = 'e';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).sname = 'File Selector (Batch Mode): Selected Files (^strict_spike)';
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).src_exbranch = substruct('.','val', '{}',{12}, '.','val', '{}',{1});
matlabbatch{13}.spm.stats.fmri_spec.sess(6).multi_reg(1).src_output = substruct('.','files');
matlabbatch{13}.spm.stats.fmri_spec.sess(6).hpf = 128;
matlabbatch{13}.spm.stats.fmri_spec.fact = struct('name', {}, 'levels', {});
matlabbatch{13}.spm.stats.fmri_spec.bases.hrf.derivs = [0 0];
matlabbatch{13}.spm.stats.fmri_spec.volt = 1;
matlabbatch{13}.spm.stats.fmri_spec.global = 'None';
matlabbatch{13}.spm.stats.fmri_spec.mask = {b.explicitMask};
matlabbatch{13}.spm.stats.fmri_spec.cvi = 'AR(1)';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1) = cfg_dep;
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).tname = 'Select SPM.mat';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).tgt_spec{1}(1).name = 'filter';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).tgt_spec{1}(1).value = 'mat';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).tgt_spec{1}(2).name = 'strtype';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).tgt_spec{1}(2).value = 'e';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).sname = 'fMRI model specification: SPM.mat File';
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).src_exbranch = substruct('.','val', '{}',{13}, '.','val', '{}',{1}, '.','val', '{}',{1});
matlabbatch{14}.spm.stats.fmri_est.spmmat(1).src_output = substruct('.','spmmat');
matlabbatch{14}.spm.stats.fmri_est.method.Classical = 1;

end

%%%%CONTRAST FUNCTIONS%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [] = batch_contrasts(b)
%This function evaluates a set of previously-defined t-contrasts. Adapted
%from fmri_contrasts_b (Ken Roberts, Duke Univ, CCN)

%load SPM
load(strcat(b.analysisDir,'SPM.mat'));

%create xCon structures for each con
% what is the range of this batch of contrasts?
if ~isempty(SPM.xCon) && b.replace_cons~=1
    num_existing_cons = length(SPM.xCon); %can modify this to overwrite
else
    num_existing_cons = 0;
    SPM.xCon = struct( 'name',{{'init'}}, 'STAT', [1], 'c', [1], 'X0', [1], ...
        'iX0', {{'init'}}, 'X1o', [1], 'eidf', [], 'Vcon', [],  'Vspm', [] );
end;

%load in contrast vectors and names
load(strcat(b.analysisDir,b.analysisName,'_',b.curSubj,b.cons));
num_cons_tocalc = length(contrast_vectors);
sessionmeans = zeros(1,length(b.taskruns));

%update xCon structures
for iCon = 1:num_cons_tocalc
    SPM.xCon(iCon + num_existing_cons) = spm_FcUtil('Set', contrast_names{iCon}, ...
        'T', 'c', transpose([contrast_vectors{iCon} sessionmeans]), SPM.xX.xKXs);
end;

%evaluate contrasts
Ci = num_existing_cons+1:(num_existing_cons + num_cons_tocalc);
spm_contrasts(SPM, Ci);

end

