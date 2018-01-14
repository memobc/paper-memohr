clear all;

% analysis info
subjects = {'s04' 's05' 's06' 's07' 's08' 's09' 's10' 's11' 's13' 's14' 's16' 's17' 's18' 's19' 's20' 's21' 's22' 's23' 's25' 's26' 's27' 's28'};
analysisName = 'ItemSourceDM_rf_new';
outLabel = ['ashs_' analysisName ];
num_cons = 9; % will extract contrast values for first num_cons contrasts

% ROI info
ROIs = {'BLA_L' 'CeM_L' 'MedA_L' 'CorA_L' 'AMY_L' ...
    'BLA_R' 'CeM_R' 'MedA_R' 'CorA_R' 'AMY_R' ...
    'wHipp_L' 'wHipp_R' ...
    'wHipp_head_L' 'wHipp_head_R' ...
    'CA1_body_L' 'CA23DG_body_L' 'subiculum_body_L' ...
    'wHipp_body_L' 'wHipp_tail_L' ...
    'CA1_body_R' 'CA23DG_body_R' 'subiculum_body_R' ...
    'wHipp_body_R' 'wHipp_tail_R' ...
    'PRC_L' 'PRC_R' 'PHC_L' 'PHC_R'};
maskDir = '/Volumes/External/MemoHR/Data/MRI/segmentation_complete/';

% directory info
ana_dir = ['/Volumes/External/MemoHR/Analysis/' analysisName '/'];
output_dir = '/Volumes/External/MemoHR/Analysis/ROI_estimates/';
if ~exist(output_dir,'dir')
    mkdir(output_dir);
end

% Initialize counter
cnt = 2;

for curROI = 1:length(ROIs);
    fprintf('Starting %s\n',ROIs{curROI})
    [a,ROIname,c] = fileparts(ROIs{curROI});
    output(1,1) = {'subject'};
    output(1,2) = {'roi_file'};
    output(1,3) = {'contrast'};
    output(1,4) = {'activity'};
    output(1,5) = {'numvox'};
    
    
    for  curSub = 1:length(subjects)
        
        % Get subject-specific ROI mask filename
        fprintf('Working on %s\n',subjects{curSub})
        curMask = [maskDir subjects{curSub} '/complete_seg/rseg_' ROIs{curROI} '.nii']; % add r for resliced
        
        % Read in mask
        [roi_y, roi_xyz] = spm_read_vols(spm_vol(curMask));
        
        % load SPM.mat file
        load([ana_dir subjects{curSub} '/SPM.mat']);
        if length(SPM.xCon) < num_cons
            error('Cannot find correct number of contrasts.');
        end
        
        for curCon = 1:num_cons
            
            % Get contrast info
            conLabel = SPM.xCon(curCon).name;
            conFile = SPM.xCon(curCon).Vcon.fname;
            
            % Get contrast values within the mask
            [con_y, con_xyz] = spm_read_vols(spm_vol([ana_dir subjects{curSub} '/' conFile]));
            
            if size(con_y,1)~=size(roi_y,1) || size(con_y,2)~=size(roi_y,2) || size(con_y,3)~=size(roi_y,3)
                error('contrast image and ROI image are not the same dimensions.')
            end
            
            t = con_y(roi_y > 0);
            t = t(~isnan(t));
            
            % Create output matrix
            output(cnt,1) = subjects(curSub);
            output(cnt,2) = {ROIname};
            output(cnt,3) = {conLabel};
            output(cnt,4) = {mean(t)};
            output(cnt,5) = {length(t)};
            
            clear t con_y con_xyz conLabel conFile
            cnt = cnt + 1;
            
        end
        
        %Increment counter and reset for next subject
        clear roi_y roi_xyz SPM
        
    end
end

% Write out results
cd(output_dir)
cell2csv(strcat('cons_',outLabel,'.csv'),output); %using excel on mac, cell2csv from FileExchange