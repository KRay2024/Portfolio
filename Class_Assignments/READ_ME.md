# Personal Projects ReadMe

## 1. DSC43C8 Project 1

- This was the first group project for my DSC 43C8 - Big Data course. In this assignment, we used t-SNE, UMAP, PHATE, PCA, sPCA, SVM, LLE,
  KMeans, and NearestNeighbors. The data sets we were working with were the Iris data set, a Big Patent data set, Drug Discovery data set,
  and an HFT dataset. I was personally responsible for all Iris and Big Patent data code.

  - IRIS: We used PCA, sPCA, t-SNE, UMAP, and LLE to visualize the data. After visualizing, we then used NearestNeighbors to caluclate the
    locality conservation ratio (LCR) for each method under four different normalizations: StandardScaler, MinMaxScaler, MaxAbsScaler,
    and RobustScaler.

  - BIG PATENT: Using a big data data set consisting of patents. For this problem we used the same four separate normalization methods.
    With each normalization method, we visualized the data using PCA and obtained the top twenty outlier patents using the PCA visualization.
    After visualizing and finding outliers with PCA, we used t-SNE and UMAP before fitting a KMeans classification model to the data to make
    predictions, analyzing the results. The metrics we used to analyze the models were: accuracy, sensitivity, specificity, precision,
    negative prediction ratio (NPR), f1-score, f1-micro, f1-macro, d-index, balanced accuracy, mutual information (MI), and adjusted mutual
    information (AMI) scores. Then, we used PHATE along with KMeans to perform the same analysis on the data using PHATE instead of t-SNE or
    UMAP. Finally, we used a stacked PCA + t-SNE method on the data this time with an SVM classification model. We used the same metrics to
    evaluate the SVM model as we did the KMeans models.

## 2. DSC43C8 Homework 1

- This was the first homework assignment for my Big Data course. In this assignment, we worked with a vehicles dataset. The first step for this
  assignment was to clean the data, checking for any columns whose values were all equal to zero, dropping those columns. Next, I combined
  the columns pertaining to different types of vehicles (SUV, Pickup, etc.) into one column, giving us our target column. For this assignment,
  we were assigned to use five different normalization methods. I chose to work with StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler,
  and Normalizer, all from the sklearn.preprocessing package.
  
  - PCA: After normalizing I used PCA to find which components explained the most variance in the data. Next, I used PCA Biplots to further
    visualize the data and identify outliers. Lastly, I found the average explained variances and average explained variance ratios under
    each normalization method. That is all for the PCA portion of this assignment.
    
  - KMEANS **|** HIERARCHICAL CLUSTERING: After PCA, I performed Hierarchical Clustering and KMeans classification on the data. For this portion
    of the assignment we were instructed to pick the highest performing normalization method, and use the normalized data from that method for
    the KMeans and Hierarchical Clustering models. The metrics used to evaluate each model were silhouette score, Calinski Harabasz score,
    AMI, and accuracy. We then were instructed to retrieve the entries from the smallest cluster. Next, we visualized the KMeans PCA clustering,
    ensuring to also plot cluster centers. Lastly, we used PCA Biplot and nSVA to retrieve the top twenty outliers from the KMeans PCA clusters.

  - PCA EXTENSIONS: For this last section, we first used sklearn.decomposition's PCA package to perform PCA on the given matrix. Next, we coded
    PCA from scratch, comparing the explained variances and variance ratios with sklearn's PCA package.

## 3. DSC43C8 Homework 2



## 4. DSC43C8 Homework 3
