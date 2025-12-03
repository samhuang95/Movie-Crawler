# Movie Crawler

這是一個用 Python 撰寫的爬蟲程式，用於抓取 [Scrape Center](https://ssr1.scrape.center/) 網站上的電影資訊。

## 功能

- 自動抓取前 10 頁的電影列表。
- 解析電影名稱、封面圖片連結、評分及類型。
- 將抓取到的資料儲存為 `movie.csv` 檔案。

## 環境安裝 (Installation)

請依照以下步驟設定開發環境：

1.  **建立虛擬環境 (Virtual Environment)**：
    建議使用虛擬環境來隔離專案套件。

    ```bash
    # Windows
    python -m venv venv
    ```

2.  **啟動虛擬環境**：

    ```bash
    # Windows (PowerShell)
    .\venv\Scripts\Activate.ps1

    # Windows (Command Prompt)
    .\venv\Scripts\activate.bat

    # macOS/Linux
    source venv/bin/activate
    ```

3.  **安裝相依套件**：
    使用 `requirements.txt` 安裝所有必要的 Python 套件。
    ```bash
    pip install -r requirements.txt
    ```

## 使用方式 (Usage)

確認虛擬環境已啟動後，執行以下指令開始爬蟲：

```bash
python crawler.py
```

程式執行完畢後，會在目錄下產生 `movie.csv` 檔案。
