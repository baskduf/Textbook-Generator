import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
import math
import random

def create_figure(ax, top_number, left_number):
    # Draw shapes
    # Top rectangle
    top_rect = patches.Rectangle((0.3, 0.55), 0.4, 0.4, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(top_rect)
    ax.text(0.5, 0.75, str(top_number), fontsize=16, ha='center', va='center')

    # Left rectangle
    left_rect = patches.Rectangle((0.05, 0.05), 0.4, 0.4, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(left_rect)
    ax.text(0.25, 0.25, str(left_number), fontsize=16, ha='center', va='center')

    # Right circle
    right_circle = patches.Circle((0.75, 0.25), 0.2, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(right_circle)

    # Draw lines
    ax.plot([0.5, 0.25], [0.55, 0.45], 'k-', lw=2)
    ax.plot([0.5, 0.75], [0.55, 0.45], 'k-', lw=2)

    # Set limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

# Generate all possible combinations
combinations = [(top, left) for top in range(2, 11) for left in range(1, top)]
random.shuffle(combinations)  # Shuffle the combinations

# Calculate number of pages needed
n_combinations = len(combinations)
n_pages = math.ceil(n_combinations / 12)  # 12 figures per page

# Set up PDF
pdf_pages = PdfPages('output.pdf')

# A4 size in inches
fig_width_in = 8.27
fig_height_in = 11.69

for page in range(n_pages):
    # Create figure with A4 size
    fig = plt.figure(figsize=(fig_width_in, fig_height_in))
    
    # Create 6x2 grid for the page
    gs = fig.add_gridspec(6, 2, wspace=0.4, hspace=0.6)
    
    for i in range(12):
        if page * 12 + i >= n_combinations:
            break
        
        # Determine position
        row = i % 6
        col = i // 6
        
        # Create subplot
        ax = fig.add_subplot(gs[row, col])
        
        # Get combination and create figure
        top, left = combinations[page * 12 + i]
        create_figure(ax, top, left)
    
    # Adjust layout and save to PDF
    plt.tight_layout()
    pdf_pages.savefig(fig)
    plt.close(fig)

# Close PDF file
pdf_pages.close()

print(f"PDF with {n_pages} pages has been created.")