package A4.kMean;

import java.util.ArrayList;
import A4.data.Iris;

//ToDo: Compute cluster mean based on cluster members.
public class KMeanCluster {

	public ArrayList<Iris> ClusterMembers;
	
	public KMeanCluster()
	{
		this.ClusterMembers = new ArrayList<Iris>();
	}
	
	@Override
	public String toString() {
		String toPrintString = "-----------------------------------CLUSTER START------------------------------------------" + System.getProperty("line.separator");
		
		for(Iris i : this.ClusterMembers)
		{
			toPrintString += i.toString() + System.getProperty("line.separator");
		}
		toPrintString += "-----------------------------------CLUSTER END-------------------------------------------" + System.getProperty("line.separator");
		
		return toPrintString;
	}

	public double calculateMean(Iris b){
		Iris a = ClusterMembers.get(0);
		double petalLength = Math.pow((a.Petal_Length - b.Petal_Length),2);
		double petalWidth = Math.pow((a.Petal_Width - b.Petal_Width),2);
		double sepalLength = Math.pow((a.Sepal_Length - a.Sepal_Length),2);
		double sepalWidth = Math.pow((a.Sepal_Length - b.Sepal_Length),2);

		Double euclideanCalculation= Math.sqrt(petalLength+petalWidth+sepalLength+sepalWidth);

		return euclideanCalculation;
	}

}
