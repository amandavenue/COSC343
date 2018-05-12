import cosc343.assig2.Creature;
import java.util.Random;

/**
* The MyCreate extends the cosc343 assignment 2 Creature.  Here you implement
* creatures chromosome and the agent function that maps creature percepts to
* actions.  
*
* @author  
* @version 1.0
* @since   2017-04-05 
*/
public class MyCreature extends Creature {

    // Random number generator
    Random rand = new Random();
    public int[] chromosome;

    /* Constructor to make a creatures chromosome.
    Chromosome is 11 ints between 1 and 100  
  
    Input: numPercept - number of percepts that creature will be receiving
          numAction - number of action output vector that creature will need
                      to produce on every turn
    */
    public MyCreature(int numPercepts, int numActions) {

        chromosome = new int [11];

        for (int i = 0; i < chromosome.length; i++){
            chromosome[i] = rand.nextInt(101);
        }
    }
    /* This function must be overridden by the MyCreature class, because it implements
        the AgentFunction which controls creature behavoiur.  This behaviour
        should be governed by the model (that you need to come up with) that is
        parameterise by the chromosome.  
  
        Input: percepts - an array of percepts
                numPercepts - the size of the array of percepts depend on the percept
                            chosen
                numExpectedAction - this number tells you what the expected size
                                    of the returned array of percepts should bes
         Returns: an array of actions 
     */
    @Override
    public float[] AgentFunction(int[] percepts, int numPercepts, int numExpectedActions) {
      
        // This is where your chromosome gives rise to the model that maps
        // percepts to actions.  This function governs your creature's behaviour.
        // You need to figure out what model you want to use, and how you're going
        // to encode its parameters in a chromosome.
      
        // At the moment, the actions are chosen completely at random, ignoring
        // the percepts.  You need to replace this code.
        float actions[] = new float[numExpectedActions];
        int numMonsters = 0;
        int avoidDirection;

        int topLeft = (chromosome[3] + chromosome[0] + chromosome[1])/3;
        int topRight = (chromosome[1] + chromosome[2] + chromosome[5])/3;
        int bottomLeft = (chromosome[3] + chromosome[6] + chromosome[7])/3;
        int bottomRight = (chromosome[5] + chromosome[8] + chromosome[9])/3;

        /*
        for(int i=0;i<numExpectedActions;i++) {
            actions[i]=rand.nextFloat();
        } 
        */

        // if creature is on edible food
        if (percepts[4] == 2){
            //eat food at the probability of chromosome[9]
            if (rand.nextInt(101) < chromosome[9]){
                actions[9] = Float.MAX_VALUE;
            }

        // if creature is on green food
        } else if (percepts[4] == 1){
            for (int i = 0; i < numPercepts; i++){
                // if there is any monsters around set the monster boolean to 
                if (i != 4 && percepts[i] == 1){
                    numMonsters++;
                }
            }
            // if there are no monsters around eatthe green food at the probability of chromosome[9]
            if (numMonsters > 0 && rand.nextInt(101) < chromosome[9]){
                actions[9] = Float.MAX_VALUE;
            }

        // if creature isnt on food but there is a monster nearby
        } else if (numMonsters == 1){
    
            // avoid based on the chromosome corresponding to the location percept
            for (int i = 0; i < numPercepts; i++){
                if (i != 4 && percepts[i] == 1 && rand.nextInt(101) < chromosome[i]){
                    if (i < 3){
                        actions[(i+5)%9] = Float.MAX_VALUE;
                    } else {
                        actions[(i+4)%9] = Float.MAX_VALUE;
                    }
                }
            }

        // multiple monsers
        } else if (numMonsters > 1){

            for(int i=0;i<numExpectedActions;i++) {
            actions[i]=rand.nextFloat();
            }

        // no monsters around
        } else {
            // if there is a berry near by move towards it if directional chromosome probability is high enough
            for(int i = 0; i < numPercepts; i++){
                if (i != 4 && percepts[i] == 3 && rand.nextInt(101) < chromosome[i]){
                    actions[i] = Float.MAX_VALUE;
                    return actions;
                }
            }
            // explore
            if (rand.nextInt(101) < chromosome[numPercepts]){
                actions[numPercepts] = Float.MAX_VALUE;
                return actions;
            }

            // random move fail case
            for(int i=0;i<numExpectedActions;i++) {
            actions[i]=rand.nextFloat();
            }

        }

        return actions;
    }
  
}