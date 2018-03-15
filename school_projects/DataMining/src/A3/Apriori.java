package A3;

import java.util.*;


public class Apriori {
	/***
	 * The TRANSACTIONS 2-dimensional array holds the full data set for the lab
	 */
    static final int[][] TRANSACTIONS = new int[][]
            {
            { 1, 2, 3, 4, 5 }, { 1, 3, 5 }, { 2, 3, 5 }, { 1, 5 }, { 1, 3, 4 }, { 2, 3, 5 }, { 2, 3, 5 },
                    { 3, 4, 5 }, { 4, 5 }, { 2 }, { 2, 3 }, { 2, 3, 4 }, { 3, 4, 5 } };
                    
    static final int[][] BOOK_TRANSACTIONS = new int[][] { { 1, 2, 5 }, {2, 4}, { 2, 3 }, { 1, 2, 4 },
            { 1, 3 }, { 2, 3 }, { 1, 3 }, { 1, 2, 3, 5 }, { 1, 2, 3 }};

    public static void main( String[] args ) {
        // TODO: Select a reasonable support threshold via trial-and-error. Can either be percentage or absolute value.
        final int supportThreshold = 2;
        apriori( TRANSACTIONS, supportThreshold );
    }

    public static List<ItemSet> apriori( int[][] transactions, int supportThreshold ) {
        int k;
        Hashtable<ItemSet, Integer> frequentItemSets = generateFrequentItemSetsLevel1( transactions, supportThreshold );

        for (k = 1; frequentItemSets.size() > 0; k++) {
            System.out.print( "Finding frequent itemsets of length " + (k + 1) + "…" );
            frequentItemSets = generateFrequentItemSets( supportThreshold, transactions, frequentItemSets );
            // TODO: add to list

            System.out.println( " found " + frequentItemSets.size() );
        }
        // TODO: create association rules from the frequent itemsets

        // TODO: return something useful
        return null;
    }

    private static Hashtable<ItemSet, Integer> generateFrequentItemSets (int supportThreshold,
                                                                         int[][] transactions,
                                                                         Hashtable<ItemSet, Integer> lowerLevelItemSet )
    {
        Hashtable<ItemSet, Integer> newLevelItemSet = new Hashtable<>();

        Object[] itemSet = lowerLevelItemSet.keySet().toArray();

        for(int i = 0; i < itemSet.length; i++)
        {
            ItemSet a = (ItemSet)itemSet[i];

            for(int j = i + 1; j < itemSet.length; j++)
            {
                ItemSet b = (ItemSet)itemSet[j];

                boolean shouldAdd = true;

                for(int z = 0; z < a.set.length - 1; z++)
                {
                    if(a.set[z] != b.set[z])
                    {
                        shouldAdd = false;
                        break;
                    }
                }

                if (shouldAdd)
                {
                    ItemSet newSet = joinSets(a, b);

                    int count = countSupport(newSet.set, transactions);

                    if (count >= supportThreshold)
                    {
                        newLevelItemSet.put(newSet, count);
                    }
                }
            }
        }

        return newLevelItemSet;
    }

    private static ItemSet joinSets( ItemSet first, ItemSet second ) {
        int[] joinedSets = new int[first.set.length + 1];

        for(int i = 0; i < first.set.length; i++)
        {
            joinedSets[i] = first.set[i];
        }
        joinedSets[joinedSets.length-1] = second.set[second.set.length-1];

        return new ItemSet(joinedSets);
    }

    private static Hashtable<ItemSet, Integer> generateFrequentItemSetsLevel1( int[][] transactions, int supportThreshold ) {
        Hashtable<ItemSet, Integer> result = new Hashtable<>();

        for(int i = 0; i < transactions.length; i++)
        {
            for (int j =  0; j < transactions[i].length; j++)
            {
                ItemSet currentItem = new ItemSet(new int[]{transactions[i][j]});
                if(!result.contains(transactions[i][j]))
                {
                    result.put(currentItem, 1);
                }
                else
                {
                    int itemCount = result.get(currentItem);
                    result.put(currentItem, itemCount+1);
                }
            }
        }

        Object[] finalResult = result.keySet().toArray();
        // checks all keys and removes those with values under the supportThreshold
        for(Object keyObj : finalResult)
        {
            ItemSet key = (ItemSet)keyObj;
            if(result.get(key) < supportThreshold)
            {
                result.remove(key);
            }
        }
        return result;
    }

    /**
     * Calculates number of times an itemset is in the dataset.
     *
     * @param itemSet       Tuple of possible transaction items
     * @param transactions  One given transaction
     * @return              The number representation of count support
     */
    public static int countSupport(int[] itemSet, int[][] transactions) {
        int count = 0;
        for(int[] transaction : transactions)
        {
            int elem = 0;
            for (int item : transaction)
            {
                if(itemSet[elem] == item)
                {
                    elem++;
                    if(elem == itemSet.length)
                    {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
    }
}
