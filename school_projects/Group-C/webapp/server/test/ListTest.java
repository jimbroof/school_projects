import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static junit.framework.TestCase.assertEquals;
import static org.junit.Assert.assertTrue;


/**
 * Created by Joachim on 14/03/2018.
 */
public class ListTest {

    private List<String> strings;

    @Before
    public void setUp() {
        strings = new ArrayList<>();
    }

    @Test
    public void testAddElementSizeOne() {
        strings.add("tekst streng");

        assertEquals(strings.size(), 1);
    }

    @Test
    public void testAddElementAndRemoveSizeZero() {
        strings.add("tekst i streng");
        strings.remove(0);

        assertTrue(strings.isEmpty());
    }


}

