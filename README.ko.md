<!-- Language Selection -->
English ([README.en.md](README.en.md)) | 한국어

# Google 이미지용 Selenium 이미지 크롤러

이 프로젝트는 Selenium을 활용하여 Google 이미지에서 이미지를 크롤링하고 다운로드하는 과정을 자동화하는 Python 스크립트를 제공합니다. 사용자는 검색어, 다운로드할 이미지 수, 이미지를 저장할 대상 디렉토리를 지정할 수 있습니다.

## 기능

*   **자동화된 이미지 검색:** 주어진 검색어에 대해 Google 이미지를 자동으로 검색합니다.
*   **동적 콘텐츠 로딩:** 페이지를 아래로 스크롤하여 더 많은 이미지를 로드하고, 지연 로딩 콘텐츠를 처리합니다.
*   **다운로드 설정 가능:** 다운로드할 최대 이미지 수를 지정할 수 있습니다.
*   **사용자 지정 출력 디렉토리:** 다운로드한 이미지를 사용자가 정의한 디렉토리에 저장합니다.

## 필수 조건

스크립트를 실행하기 전에 다음이 설치되어 있는지 확인하십시오:

*   **Python 3.x:** 스크립트는 Python으로 작성되었습니다.
*   **pip:** Python 패키지 설치 관리자 (일반적으로 Python과 함께 제공됩니다).
*   **Google Chrome 또는 Chromium 브라우저:** Selenium은 웹 브라우저를 자동화하는 데 필요합니다.
*   **ChromeDriver:** Chrome용 WebDriver. **ChromeDriver 버전이 Chrome 브라우저 버전과 일치하는 것이 중요합니다.**

## 설치

1.  **저장소 복제 (아직 하지 않았다면):**
    ```bash
    git clone https://github.com/your-username/selenium-image-crawling.git
    cd selenium-image-caching
    ```
    (참고: 이 프로젝트가 GitHub에 호스팅되어 있다면 `your-username`을 실제 GitHub 사용자 이름으로 바꾸십시오.)

2.  **Python 종속성 설치:**
    ```bash
    pip install selenium
    ```

## ChromeDriver 설정

1.  **Chrome 브라우저 버전 확인:**
    Chrome을 열고 `chrome://version/`으로 이동하여 Chrome 버전 번호를 확인하십시오.

2.  **호환되는 ChromeDriver 다운로드:**
    [ChromeDriver 다운로드](https://chromedriver.chromium.org/downloads) 페이지를 방문하십시오. Chrome 브라우저 버전과 일치하는 ChromeDriver 버전을 다운로드하십시오.

3.  **ChromeDriver를 PATH에 추가:**
    *   **Linux/macOS:** 다운로드한 `chromedriver` 실행 파일을 시스템의 PATH에 있는 디렉토리 (예: `/usr/local/bin`)로 이동하십시오.
        ```bash
        sudo mv /path/to/your/downloaded/chromedriver /usr/local/bin/
        sudo chmod +x /usr/local/bin/chromedriver
        ```
    *   **Windows:** `chromedriver.exe`를 시스템의 PATH 환경 변수에 포함된 디렉토리에 배치하거나, `google.py` 스크립트와 동일한 디렉토리에 배치하십시오.

## 사용법

터미널에서 스크립트를 실행하십시오.

```bash
python google.py <검색어> [이미지_수] [다운로드_디렉토리]
```

**인수:**

*   `<검색어>` (필수): Google 이미지에서 검색할 키워드. 여러 단어 검색어는 따옴표로 묶으십시오. 예를 들어, "아름다운 풍경"과 같이 사용합니다.
*   `[이미지_수]` (선택 사항): 다운로드할 최대 이미지 수. 지정하지 않으면 스크립트는 기본값 (일반적으로 100개 정도, `google.py`에서 확인)을 다운로드하려고 시도합니다.
*   `[다운로드_디렉토리]` (선택 사항): 이미지가 저장될 디렉토리 경로. 지정하지 않으면 이미지는 현재 작업 디렉토리 내의 검색어 이름으로 된 디렉토리에 저장됩니다.

**예시:**

1.  **"cats"를 검색하고 기본 디렉토리에 다운로드:**
    ```bash
    python google.py cats
    ```

2.  **"dogs"를 검색하고 50개 이미지 다운로드:**
    ```bash
    python google.py dogs 50
    ```

3.  **"beautiful landscapes"를 검색하고 특정 폴더에 저장:**
    ```bash
    python google.py "beautiful landscapes" 100 ./my_landscape_images
    ```

## 문제 해결

*   **`selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.`**
    이 오류는 ChromeDriver를 찾을 수 없음을 의미합니다. 올바른 버전을 다운로드하여 시스템의 PATH에 배치했거나 `google.py`와 동일한 디렉토리에 배치했는지 확인하십시오.

*   **`selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX`**
    이것은 버전 불일치 오류입니다. ChromeDriver 버전이 Chrome 브라우저 버전과 일치하지 않습니다. 올바른 ChromeDriver 버전을 다운로드하십시오.

## 원본 가이드

*   **블로그 게시물:** [https://open-support.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C](https://open-support.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%9D%B4%EB%AF%B8%EC%A7%80-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C)
*   **YouTube 비디오:** [https://www.youtube.com/watch?v=1b7pXC1-IbE&list=PLU9-uwewPMe2-vtJAgWB6SNhHcTjJDgEO&index=2](https://www.youtube.com/watch?v=1b7pXC1-IbE&list=PLU9-uwewPMe2-vtJAgWB6SNhHcTjJDgEO&index=2)

## 라이센스

이 프로젝트는 [LICENSE](LICENSE) 파일에 따라 라이센스가 부여됩니다.