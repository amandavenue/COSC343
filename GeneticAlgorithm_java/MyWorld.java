import cosc343.assig2.World;
import cosc343.assig2.Creature;
import java.util.*;
import java.io.*;

/**
* The MyWorld extends the cosc343 assignment 2 World.  Here you can set 
* some variables that control the simulations and override functions that
* generate populations of creatures that the World requires for its
* simulations.
*
* @author  
* @version 1.0
* @since   2017-04-05 
*/
public class MyWorld extends World {
 
	/* Here you can specify the number of turns in each simulation
	* and the number of generations that the genetic algorithm will 
	* execute.
	*/
	private final int _numTurns = 100;
	private final int _numGenerations = 500;
  
  	// initialise arrays for potential parents and elite for selection
	ArrayList<MyCreature> potentialParents = new ArrayList<MyCreature>();
	ArrayList<MyCreature> potentialEliteParents = new ArrayList<MyCreature>();

	Random rand = new Random();

	// set the percentage governing mutation
	public static final double MUTATIONPERCENT = 0.06;
  
	/* Constructor.  
   
		Input: worldType - specifies which simulation will be running
			griSize - the size of the world
			windowWidth - the width (in pixels) of the visualisation window
			windowHeight - the height (in pixels) of the visualisation window
			repeatableMode - if set to true, every simulation in each
							 generation will start from the same state
	*/
	public MyWorld(int worldType, int gridSize, int windowWidth, int windowHeight, boolean repeatableMode) {   
	   	// Initialise the parent class - don't remove this
	   	super(worldType, gridSize, windowWidth,  windowHeight, repeatableMode);

	   	// Set the number of turns and generations
	   	this.setNumTurns(_numTurns);
	   	this.setNumGenerations(_numGenerations);
	  
	  
	}
 
	/* The main function for the MyWorld application

	*/
	public static void main(String[] args) {
	  	// Here you can specify the grid size, window size and whether to run
	   	// in repeatable mode or not
	   	int gridSize = 29; // 29 for 50 creatures, 41 for 100
	   	int windowWidth =  1600;
	   	int windowHeight = 900;
	   	boolean repeatableMode = false;
	 
	   	/* Here you can specify world type - there are two to
		 choose from: 1 and 2.  Refer to the Assignment2 instructions for
		 explanation of the world type formats.
	   	*/
	   	int worldType = 1;     
	 
	   	// Instantiate MyWorld object.  The rest of the application is driven
	   	// from the window that will be displayed.
	   	MyWorld sim = new MyWorld(worldType, gridSize, windowWidth, windowHeight, repeatableMode);
	}
  

	/* The MyWorld class must override this function, which is
	 used to fetch a population of creatures at the beginning of the
	 first simulation.  This is the place where you need to  generate
	 a set of creatures with random behaviours.
  
	 Input: numCreatures - this variable will tell you how many creatures
						   the world is expecting
							
	 Returns: An array of MyCreature objects - the World will expect numCreatures
			  elements in that array     
	*/  
	@Override
	public MyCreature[] firstGeneration(int numCreatures) {

	   	int numPercepts = this.expectedNumberofPercepts();
	   	int numActions = this.expectedNumberofActions();
	  
	   	// This is just an example code.  You may replace this code with
	   	// your own that initialises an array of size numCreatures and creates
	   	// a population of your creatures
	   	MyCreature[] population = new MyCreature[numCreatures];
	   	for(int i=0;i<numCreatures;i++) {
			population[i] = new MyCreature(numPercepts, numActions);     
		}
		return population;
  	}

  	/* Calculates the fitness of a creature for reproduction purposes
	
		Input : energy - energy at time of death/end of simulation
				dead - boolean to say if a creature died or not
				turns - number of turns before a creature died

		Returns : an int corresponding to its fitness rating
	*/

  	public int calculateFitness(int energy, Boolean dead){
  		int fitness = 0;

  		if (!dead){
  			// if the creature survived the simulation set its fitness to 500
  			return 500;
  		} else {
  			// otherwise set its fitness to its final energy
  			fitness = energy;
  		}

  		return fitness;
  	}

  	/* Mutates a randomly selected gene of a creature

  		Input : mutatee - the creature who is to have a gene mutated

  		Returns : the same creature with its gene mutated
  	*/

  	public MyCreature mutation(MyCreature mutatee){
  		int gene = rand.nextInt(11);

  		// mutate the randomly selected gene of the mutatee (flip the number eg. 90 -> 10)
  		mutatee.chromosome[gene] = 100 - mutatee.chromosome[gene];
  		return mutatee;
  	}

	/* Selects the fittest parent from the list of potential parents

  		Input : a boolean to indicate if elitism is being used

  		Returns : the index of the fittest parent from within the potential parents
  	*/

  	public int fittestParent(Boolean elitism){

  		int maxFitness = 0;
  		int fittestIndex = -1;

  		//yes elitism, use potentialEliteParents list
  		if (elitism){
  			// work out what the maximum fitness of the potential elite population is 
	  		for (int i = 0; i < potentialEliteParents.size(); i++){
	  			MyCreature current = potentialEliteParents.get(i);
	  			if (calculateFitness(current.getEnergy(), current.isDead()) > maxFitness){
	  				maxFitness = calculateFitness(current.getEnergy(), current.isDead());
	  			}
	  		}
	  		// locate which individual had the maximum fitness
	  		for (int i = 0; i < potentialEliteParents.size(); i++){
	  			MyCreature current = potentialEliteParents.get(i);
	  			if (calculateFitness(current.getEnergy(), current.isDead()) == maxFitness){
	  				fittestIndex = i;
	  			}
	  		}
	  		// return the index of the fittest parent
  			return fittestIndex;

  		//no elitism, use potentialParents list
  		} else {
  			// work out what the maximum fitness of the potential population is 
  			for (int i = 0; i < potentialParents.size(); i++){
	  			MyCreature current = potentialParents.get(i);
	  			if (calculateFitness(current.getEnergy(), current.isDead()) > maxFitness){
	  				maxFitness = calculateFitness(current.getEnergy(), current.isDead());
	  				fittestIndex = i;
	  			}
	  		}
	  		// locate which individual had the maximum fitness
	  		for (int i = 0; i < potentialParents.size(); i++){
	  			MyCreature current = potentialParents.get(i);
	  			if (calculateFitness(current.getEnergy(), current.isDead()) == maxFitness){
	  				fittestIndex = i;
	  			}
	  		}
	  		// return the index of the fittest parent
	  		return fittestIndex;
  		}
  	}

	/* Performs the crossover algorithm on two parents to produce a child

  		Input : two creatures, parent one and parent two

  		Returns : a child creature with a combination of the parents genes
  	*/

  	public MyCreature crossOver (MyCreature parent1, MyCreature parent2){

  		int numPercepts = this.expectedNumberofPercepts();
	   	int numActions = this.expectedNumberofActions();

	   	// create a new child
  		MyCreature child = new MyCreature(numPercepts, numActions);

  		// select that random crossver point
  		int point = rand.nextInt(11);

  		//populate the first half of the childs chromosome with parent one's genes
  		for (int i = 0; i <= point; i++){
  			child.chromosome[i] = parent1.chromosome[i];
  		}

  		//populate the second half of the childs chromosome with parent two's genes
  		for (int i = point; i < parent1.chromosome.length; i++){
  			child.chromosome[i] = parent2.chromosome[i];
  		}

  		// mutate the chlds chromosome at the probability of MUTATIONPERCENT
  		if (rand.nextDouble() < MUTATIONPERCENT){
  			child = mutation(child);
  		}

  		return child;

  	}
  
  	/* The MyWorld class must override this function, which is
	 used to fetch the next generation of creatures.  This World will
	 proivde you with the old_generation of creatures, from which you can
	 extract information relating to how they did in the previous simulation...
	 and use them as parents for the new generation.
  
	 Input: old_population_btc - the generation of old creatures before type casting. 
							  The World doesn't know about MyCreature type, only
							  its parent type Creature, so you will have to
							  typecast to MyCreatures.  These creatures 
							  have been participating in a simulation and their state
							  can be queried to evaluate their fitness
			numCreatures - the number of elements in the old_population_btc
						   array
						
							
  	Returns: An array of MyCreature objects - the World will expect numCreatures
		   elements in that array.  This is the new population that will be
		   used for the next simulation.  
  	*/  
  	@Override
  	public MyCreature[] nextGeneration(Creature[] old_population_btc, int numCreatures) {
		// Typcast old_population of Creatures to array of MyCreatures
	 	MyCreature[] old_population = (MyCreature[]) old_population_btc;
	 	// Create a new array for the new population
	 	MyCreature[] new_population = new MyCreature[numCreatures];

	 	// create a list to be populated with the chosen elite creatures
	 	ArrayList<MyCreature> eliteCreatures = new ArrayList<MyCreature>();

	  	MyCreature child;
	  	// indexes of both parents
	  	int parent1, parent2;
	  	// set the maximum number of elite creatures allowed in the next generation
	 	int elitismMax = (int)(numCreatures*0.10);

	 	//populate the list of potential parents and 
	 	// potential elite parents with the current population
	 	for (int i = 0; i < old_population.length; i++){
	 		potentialParents.add(old_population[i]);
	 		potentialEliteParents.add(old_population[i]);
	 	}
	 
	 	// Here is how you can get information about the old creatures and how
	 	// well they did in the simulation
	 	float avgLifeTime=0f;
	 	int nSurvivors = 0;
	 	int avgFitness = 0;
	 	for(MyCreature creature : old_population) {
			// The energy of the creature.  This is zero if a creature starved to
			// death, non-negative otherwise.  If this number is non-zero, but the 
			// creature is dead, then this number gives the energy of the creature
			// at the time of death.
			int energy = creature.getEnergy();

			// This querry can tell you if the creature died during the simulation
			// or not.  
			boolean dead = creature.isDead();
		
			if(dead) {
		   		// If the creature died during simulation, you can determine
		   		// its time of death (in units of turns)
		   		int timeOfDeath = creature.timeOfDeath();
		   		avgLifeTime += (float) timeOfDeath;
			} else {
		   		nSurvivors += 1;
		   		avgLifeTime += (float) _numTurns;
		   		avgFitness += calculateFitness(energy, dead);
			}

	 	}

	 	// Right now the information is used to print some stats...but you should
	 	// use this information to access creatures' fitness.  It's up to you how
	 	// you define your fitness function.  You should add a print out or
	 	// some visual display of the average fitness over generations.
	 	avgLifeTime /= (float) numCreatures;
	 	//System.out.println("Simulation stats:");
	 	//System.out.println("  Survivors    : " + nSurvivors + " out of " + numCreatures);
	 	//System.out.println("  Avg life time: " + avgLifeTime + " turns");
	 	avgFitness /= (float) numCreatures;
	 	System.out.println("Average fitness: " + avgFitness);

	 	// populate the new population with children
	 	for (int i = 0; i < old_population.length; i++){
	 		// if we still have elite creatures to add
	 		if (i < elitismMax){
	 			// select the fittest creature from the last population
	 			parent1 = fittestParent(true);
	 			// add this parent
	 			new_population[i] = potentialEliteParents.get(parent1);
	 			// remove it from the potential elite parents list
	 			potentialEliteParents.remove(parent1);
	 		// if we have reached the maximum number of elite in our new population
	 		} else {
	 			// generate the two fittest parents
	 			parent1 = fittestParent(false);
	 			parent2 = fittestParent(false);
	 			// generate the child and add it to the new population
	 			child = crossOver(potentialParents.get(parent1), potentialParents.get(parent2));
	 			new_population[i] = child;
	 			// remove the first parent from the list of potential parents
	 			potentialParents.remove(parent1);
	 		}
	 	}

	 
	 	// Return new population of creatures.
	 	return new_population;
  	}
  
}