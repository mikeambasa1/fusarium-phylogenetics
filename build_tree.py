from Bio import AlignIO, Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
import matplotlib.pyplot as plt

# Step 1: Read the alignment
# Hint: AlignIO.read() needs two arguments - the filename, and the format ("fasta")
alignment = AlignIO.read("fusarium_aligned.fa", "fasta")

# Print how many sequences it loaded, and how long the alignment is
print("Number of sequences:", len(alignment))
print("Alignment length:", alignment.get_alignment_length())

# Step 2: Calculate distances between every pair of sequences
# Hint: DistanceCalculator takes a model name as a string - use "identity" for a simple start
calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

# Step 3: Build the tree using Neighbor-Joining
# Hint: DistanceTreeConstructor().nj() takes the distance_matrix as its argument
constructor = DistanceTreeConstructor()
tree = constructor.nj(distance_matrix)

# Step 4: Draw the tree
fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes, do_show=False)
plt.savefig("fusarium_tree.png", dpi=150)
plt.show()