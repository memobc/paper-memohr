### Script for saving out model regressor csv files
### Author: Maureen Ritchey 2016

# Load data ----
subjects <- c('s04','s05','s06','s07','s08','s09','s10','s11','s12',
              's13','s14','s15','s16','s17','s18',
              's19','s20','s21','s22','s23','s24','s25','s26','s27','s28') 
datadir <- '/Volumes/External/MemoHR/Data/Behavioral/'
plotdir <- paste(datadir,'summary/',sep='')
modelName <- 'ItemSourceDM'

library('ggplot2')

load(paste(plotdir,"processedData.Rdata",sep=""))

# WRITE OUT FILES -------------------------------------------------------------
#' Save out data
#' =====
trinums <- NULL
for (sub in subjects) {
  
  outputdata.sub <- subset(outputdata,participant==as.numeric(substring(sub,2,3))) 
  
  # Create new columns indexing model regressors ----------
  
  ### ItemSourceDm model: EmoR-SC, EmoR-SI, EmoK, EmoM, NeuR-SC, NeuR-SI, NeuK, NeuM, Other ----
  output.enc <- outputdata.sub[!is.na(outputdata.sub$runs.thisN),]
  output.enc <- output.enc[order(output.enc$runs.thisN,output.enc$trials.thisN.E),]
  reg <- factor(rep(NA,nrow(output.enc)),levels=c('EmoR-SC','EmoR-SI','EmoK','EmoM','NeuR-SC','NeuR-SI','NeuK','NeuM','Other'))
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Emo" & output.enc$itemScore=="Rec" & output.enc$sourceScore.sure=="Correct"] <- "EmoR-SC"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Emo" & output.enc$itemScore=="Rec" & output.enc$sourceScore.sure=="Incorrect"] <- "EmoR-SI"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Emo" & (output.enc$itemScore=="Fam" ) ] <- "EmoK"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Emo" & (output.enc$itemScore=="Miss") ] <- "EmoM"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Neu" & output.enc$itemScore=="Rec" & output.enc$sourceScore.sure=="Correct"] <- "NeuR-SC"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Neu" & output.enc$itemScore=="Rec" & output.enc$sourceScore.sure=="Incorrect"] <- "NeuR-SI"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Neu" & (output.enc$itemScore=="Fam") ] <- "NeuK"
  reg[output.enc$TrialType=="Old" & output.enc$EmotionType=="Neu" & (output.enc$itemScore=="Miss")] <- "NeuM"
  reg[output.enc$TrialType=="Old" & (is.na(output.enc$itemScore))] <- "Other"
  reg[output.enc$TrialType=="Old" & output.enc$itemScore=="Rec" & (is.na(output.enc$sourceScore.sure))] <- "Other"
  summary(reg)
  
  # Write out files with model information (names, onsets, runs)
  modeldata <- data.frame(run=output.enc$runs.thisN,onset=output.enc$onsetTimeTrial,regID=as.numeric(reg),regName=reg)
  modelFilename <- paste0(datadir,sub,'/',sub,'_',modelName,'.csv')
  write.csv(modeldata,file=modelFilename)
  
  # Save plot of model onsets
  p <- qplot(regName,onset,data=modeldata,color=regName,facets=.~run,main=sub) +
    ylim(c(max(modeldata$onset),0)) + geom_point(size=3) + theme_gray(10) +
    theme(axis.title.x=element_blank(),axis.text.x=element_blank(),axis.ticks.x=element_blank())
  print(p)
  ggsave(filename=paste0(datadir,sub,'/',sub,'_',modelName,'.pdf'),width=12,height=6)
  
  # Keep track of trial numbers
  trinums <- rbind(trinums,c(sub,summary(modeldata$regName)))
  
}

print(as.data.frame(trinums))
modelFilename <- paste0(datadir,modelName,'_trialNumbers.csv')
write.csv(as.data.frame(trinums),file=modelFilename)

