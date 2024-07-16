import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

def create_table(ax, x_offset, y_offset):
    number = random.randint(11, 20)
    
    # 2x5 표 그리기
    for i in range(4):
        for j in range(5):
            rect = plt.Rectangle((x_offset + j, y_offset + 1-i), 1, 1, fill=False, edgecolor='black')
            ax.add_patch(rect)
    
    # 원 채우기
    for k in range(number):
        row = k // 5
        col = k % 5
        circle = plt.Circle((x_offset + col + 0.5, y_offset + 1.5 - row), 0.4, color='blue')
        ax.add_patch(circle)
    
    # 숫자 표시
    #ax.text(x_offset + 5.2, y_offset + 1, str(number), va='center', fontsize=10)

def create_page():
    fig, ax = plt.subplots(figsize=(8.27, 11.69))  # A4 size in inches
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 25)
    ax.axis('off')

    # 좌측 5개 표 생성
    for i in range(5):
        create_table(ax, 0, i*4.5)

    # 우측 5개 표 생성
    for i in range(5):
        create_table(ax, 9, i*4.5)

    plt.tight_layout()
    return fig

# 사용자로부터 페이지 수 입력 받기
num_pages = int(input("몇 페이지를 생성하시겠습니까? "))

pdf_filename = 'random_tables.pdf'
with PdfPages(pdf_filename) as pdf:
    for _ in range(num_pages):
        fig = create_page()
        pdf.savefig(fig)
        plt.close(fig)

# 저장된 파일의 전체 경로 출력
full_path = os.path.abspath(pdf_filename)
print(f"{num_pages}페이지가 생성되어 다음 위치에 저장되었습니다:")
print(full_path)

print(f"{num_pages}페이지가 생성되어 'random_tables.pdf' 파일로 저장되었습니다.")