Question 

Using devices such as Jawbone Up, Nike FuelBand, and Fitbit it is now possible to collect a large amount of data about personal activity relatively inexpensively. These type of devices are part of the quantified self movement - a group of enthusiasts who take measurements about themselves regularly to improve their health, to find patterns in their behavior, or because they are tech geeks. One thing that people regularly do is quantify how much of a particular activity they do, but they rarely quantify how well they do it. In this project, our goal will be to use data from accelerometers on the belt, forearm, arm, and dumbell of 6 participants. They were asked to perform barbell lifts correctly and incorrectly in 5 different ways. More information is available from the website here: http://groupware.les.inf.puc-rio.br/har (see the section on the Weight Lifting Exercise Dataset)

library(rattle)
Rattle: A free graphical interface for data science with R.
Version 5.2.0 Copyright (c) 2006-2018 Togaware Pty Ltd.
Type 'rattle()' to shake, rattle, and roll your data.
    > library(caret)
Loading required package: lattice
Loading required package: ggplot2
    > library(rpart)
    > library(rpart.plot)
    > library(corrplot)
corrplot 0.84 loaded
    > library(randomForest)

randomForest 4.6-14

Type rfNews() to see new features/changes/bug fixes.

Attaching package: ‘randomForest’

The following object is masked from ‘package:ggplot2’: margin

The following object is masked from ‘package:rattle’: importance

    > library(RColorBrewer)
    > set.seed(56789)
    > setwd(".")
    > trainFile <- "./pml-training.csv"
    > testFile  <- "./pml-testing.csv"
    > trainRaw <- read.csv(trainFile)
    > testRaw <- read.csv(testFile)
    > dim(trainRaw)
    > dim(trainRaw)

[1] 19622   160
    
    > dim(testRaw)
[1]  20 160

    > NZV <- nearZeroVar(trainRaw, saveMetrics = TRUE)
    > head(NZV, 20)
                       freqRatio percentUnique zeroVar   nzv
    X                       1.000000  100.00000000   FALSE FALSE
    user_name               1.100679    0.03057792   FALSE FALSE
    raw_timestamp_part_1    1.000000    4.26562022   FALSE FALSE
    raw_timestamp_part_2    1.000000   85.53154622   FALSE FALSE
    cvtd_timestamp          1.000668    0.10192641   FALSE FALSE
    new_window             47.330049    0.01019264   FALSE  TRUE
    num_window              1.000000    4.37264295   FALSE FALSE
    roll_belt               1.101904    6.77810621   FALSE FALSE
    pitch_belt              1.036082    9.37722964   FALSE FALSE
    yaw_belt                1.058480    9.97349913   FALSE FALSE
    total_accel_belt        1.063160    0.14779329   FALSE FALSE
    kurtosis_roll_belt   1921.600000    2.02323922   FALSE  TRUE
    kurtosis_picth_belt   600.500000    1.61553358   FALSE  TRUE
    kurtosis_yaw_belt      47.330049    0.01019264   FALSE  TRUE
    skewness_roll_belt   2135.111111    2.01304658   FALSE  TRUE
    skewness_roll_belt.1  600.500000    1.72255631   FALSE  TRUE
    skewness_yaw_belt      47.330049    0.01019264   FALSE  TRUE
    max_roll_belt           1.000000    0.99378249   FALSE FALSE
    max_picth_belt          1.538462    0.11211905   FALSE FALSE
    max_yaw_belt          640.533333    0.34654979   FALSE  TRUE

    > training01 <- trainRaw[, !NZV$nzv]
    > testing01 <- testRaw[, !NZV$nzv]
    > dim(training01)
[1] 19622   100

    > dim(testing01)
[1]  20 100
    
    > rm(trainRaw)
    > rm(testRaw)
    > rm(NZV)
    > regex=grepl("^X|timestamp|user_name", names(training01))
    > training <- training01[, !regex]
    > testing <- testing01[, !regex]
    > rm(regex)
    > rm(training01)
    > rm(testing01)
    > dim(training)

[1] 19622    95
    > dim(testing)

[1] 20 95

    > cond <- (colSums(is.na(training)) == 0)
    > training <- training[, cond]
    > testing <- testing[, cond]
    > rm(cond)
    > corrplot(cor(training[, -length(names(training))]), method = "color", tl.cex = 0.5)


