package A4;

import java.util.ArrayList;

import A4.kMean.KMeanCluster;
import A4.kMean.KMeans;
import A4.kMedoid.KMedoid;
import A4.kMedoid.KMedoidCluster;
import A4.data.*;

public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//First step load in iris data
		ArrayList<Iris> irisData = DataLoader.LoadAllIrisData();
		
		//Second step --> do the clustering using k-means!
		ArrayList<KMeanCluster> FoundClusters_KMeans = KMeans.KMeansPartition(3, irisData);
		
		//Third step --> do the clustering using k-medoids!
		ArrayList<KMedoidCluster> FoundClusters_KMedoids = KMedoid.KMedoidPartition(3, irisData);
	}

}
