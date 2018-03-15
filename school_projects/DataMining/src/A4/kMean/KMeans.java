package A4.kMean;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import A4.data.*;


public class KMeans {

	public static ArrayList<KMeanCluster> KMeansPartition(int k, ArrayList<Iris> data)
	{


		ArrayList<KMeanCluster> kMeanClusterArrayList = irisCreator(k,data);

		for (Iris iris : data) {
			Double firstScore = kMeanClusterArrayList.get(0).calculateMean(iris);
			Double secondScore = kMeanClusterArrayList.get(1).calculateMean(iris);
			Double thirdScore = kMeanClusterArrayList.get(2).calculateMean(iris);

			if (firstScore < secondScore && firstScore < thirdScore)
				kMeanClusterArrayList.get(0).ClusterMembers.add(iris);
			else if (secondScore < firstScore && secondScore < thirdScore)
				kMeanClusterArrayList.get(1).ClusterMembers.add(iris);
			else if (thirdScore < firstScore && thirdScore < secondScore)
				kMeanClusterArrayList.get(2).ClusterMembers.add(iris);
		}

		return kMeanClusterArrayList;
	}

	public static ArrayList<KMeanCluster> irisCreator(int k, ArrayList<Iris> data) {
		ArrayList<KMeanCluster> kMeanClusterArrayList = new ArrayList<>();

		List<Integer> numberChecker = new ArrayList<>();

		for (int i = 0; i < k; i++) {
			int randomNumber = new Random().nextInt(data.size());
			Iris randomIris = data.get(randomNumber);

			if(!numberChecker.contains(randomIris)) {
				numberChecker.add(randomNumber);

				KMeanCluster kCluster = new KMeanCluster();
				kMeanClusterArrayList.add(kCluster);
				kCluster.ClusterMembers.add(randomIris);
			}
			else i--;
		}

		ArrayList<KMeanCluster> theFinal = iriscalculator(kMeanClusterArrayList, data);

		return theFinal;
	}

	public static ArrayList<KMeanCluster> iriscalculator(ArrayList<KMeanCluster> firstIteration, ArrayList<Iris> data){

		ArrayList<KMeanCluster> comparator = new ArrayList<>();

		while(!comparator.equals(firstIteration)) {

			comparator = firstIteration;

			for (Iris iris : data) {
				boolean hasChanged = false;

				Double firstScore = firstIteration.get(0).calculateMean(iris);
				Double secondScore = firstIteration.get(1).calculateMean(iris);
				Double thirdScore = firstIteration.get(2).calculateMean(iris);

				if (firstScore < secondScore && firstScore < thirdScore)
					firstIteration.get(0).ClusterMembers.add(iris);
				else if (secondScore < firstScore && secondScore < thirdScore)
					firstIteration.get(1).ClusterMembers.add(iris);
				else if (thirdScore < firstScore && thirdScore < secondScore)
					firstIteration.get(2).ClusterMembers.add(iris);
			}

			for(KMeanCluster k : firstIteration){
				for(Iris iris: k.ClusterMembers){
					double score = 0;
					score += k.calculateMean(iris);
				}
			}


		}
		return firstIteration;
	}
}
