import tabula

# PDF 경로 또는 URL
pdf_path = "https://www.samsungfund.com/etf/product/download.do?type=HOLDING&id=2ETF14"

# PDF에서 테이블 추출
df_list = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# 첫 번째 테이블만 사용
df = df_list[0]
print(df.head())