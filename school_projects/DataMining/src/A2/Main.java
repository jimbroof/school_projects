package A2;

import A2.enums.Class_Label;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Main class to run program from.
 */
public class Main {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// First step - Load data and convert to Mushroom objects.
		ArrayList<Mushroom> mushrooms = DataManager.LoadData();
		System.out.println("DataManager loaded "+mushrooms.size() + " mushrooms");

		ArrayList<Mushroom> testSet = new ArrayList<>();
		for (int i = 0; i < mushrooms.size() / 3; i++)
		{
			testSet.add(mushrooms.get(i));
		}

		ArrayList<Mushroom> trainingSet = new ArrayList<>();
		for (int i = (mushrooms.size() / 3) + 1; i < mushrooms.size(); i++)
		{
			trainingSet.add(mushrooms.get(i));
		}

		ArrayList<Object> attributesToCompare = Mushroom.getAttributeList();

		for (int i = 0; i < testSet.size(); i++)
		{
			Mushroom testMushroom = testSet.get(i);

			Map<Mushroom, Double> allDistances = new HashMap<>();

			for (int j = 0; j < trainingSet.size(); j++)
			{
				Mushroom mushroomForComparison = trainingSet.get(j);

				double distanceSum = 0;

				for (Object attribute : attributesToCompare)
				{
					Object testMushroomValue = testMushroom.getAttributeValue(attribute);
					Object mushroomForComparisonValue = mushroomForComparison.getAttributeValue(attribute);

					if (!testMushroomValue.equals(mushroomForComparisonValue))
					{
						distanceSum = distanceSum + 1;
					}
				}

				double finalDistance = Math.sqrt(distanceSum);
				allDistances.put(mushroomForComparison, finalDistance);
			}

			makeAssumption(testMushroom, allDistances);
			trainingSet.add(testMushroom);


		}


	}

	public static void makeAssumption(Mushroom mushroom, Map<Mushroom, Double> distances)
	{
		int k = 10;

		//final boss 2
		List<Mushroom> sortedMushrooms =
				distances.entrySet().stream().sorted((x, y) -> x.getValue()
				.compareTo(y.getValue())).map(Map.Entry::getKey)
				.collect(Collectors.toList());

		int edibleCount = 0;

		for (int i = 0; i < k; i++)
		{
			Mushroom closeMushroom = sortedMushrooms.get(i);

			if (closeMushroom.getAttributeValue(Class_Label.class) == Class_Label.edible)
			{
				edibleCount++;
			}
		}

		if (edibleCount > k/2)
		{
			//Assume it is edible

			//Check if it is edible
			if (mushroom.getAttributeValue(Class_Label.class) != Class_Label.edible)
			{
				System.out.println("We assumed it is edible, but it is not");
			}
		}
		else
		{
			//Assume it is poisonous

			//Check if it is poisonous
			if (mushroom.getAttributeValue(Class_Label.class) == Class_Label.edible)
			{
				System.out.println("We assumed it is poisonous, but it is edible");
			}
		}
	}

}
