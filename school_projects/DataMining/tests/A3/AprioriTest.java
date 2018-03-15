package A3;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import static junit.framework.TestCase.assertEquals;

/**
 * Testing methods for Apriori
 */
public class AprioriTest {

    private Apriori testClass = new Apriori();
    private int[][] testTransactions;
    private int[] itemSet;

    @Before
    public void setUp()
    {
        testTransactions = new int[][]{{ 1, 2, 3, 4, 5 }, { 1, 3, 5 }};
        itemSet = new int[]{1,3,5};
    }

    @After
    public void tearDown()
    {
        testTransactions = null;
        itemSet = null;
    }

    @Test
    public void testCountSupport()
    {
        assertEquals(2, testClass.countSupport(itemSet, testTransactions));
    }
}
