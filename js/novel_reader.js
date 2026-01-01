// 引入推荐的库: epubjs 用于处理电子书内容, localforage 用于存储书签
// 通过CDN或npm安装: epubjs, localforage

// 加载txt文件
function load_novel(url) {
    // 使用fetch加载txt文件内容
    fetch(url)
        .then(response => response.text())
        .then(text => {
            // 将文本内容分割成页面
            render_page(text);
        })
        .catch(error => console.error('加载小说文件失败:', error));
}

// 保存书签
function save_bookmark() {
    // 获取当前阅读位置
    const currentPos = getCurrentPosition();
    // 使用localForage保存书签到本地存储
    localforage.setItem('novel_bookmark', {
        url: window.location.href,
        position: currentPos,
        timestamp: Date.now()
    }).then(() => {
        console.log('书签已保存');
    }).catch(err => {
        console.error('保存书签失败:', err);
    });
}

// 加载书签
function load_bookmark() {
    localforage.getItem('novel_bookmark').then(bookmark => {
        if (bookmark && bookmark.url) {
            // 如果书签是当前页面的，则滚动到之前的位置
            if (bookmark.url === window.location.href) {
                window.scrollTo(0, bookmark.position || 0);
            }
        }
    }).catch(err => {
        console.error('读取书签失败:', err);
    });
}

function clear_bookmark() {
    // 清除保存的书签
    localforage.removeItem('novel_bookmark')
        .then(() => {
            console.log('书签已清除');
        })
        .catch(err => {
            console.error('清除书签失败:', err);
        });
}

// 渲染页面
function render_page(content) {
    // 如果内容未提供，则从某个地方获取
    if (!content) {
        // 这里可以是从服务器获取或从缓存中读取
        return;
    }

    // 获取阅读器容器
    const readerContainer = document.getElementById('reader-container');
    if (!readerContainer) {
        console.error('找不到阅读器容器');
        return;
    }

    // 清空容器
    readerContainer.innerHTML = '';
    
    // 创建内容容器
    const contentDiv = document.createElement('div');
    contentDiv.className = 'novel-content';
    contentDiv.textContent = content;
    readerContainer.appendChild(contentDiv);
    
    // 恢复之前的阅读位置（如果存在书签）
    localforage.getItem('novel_bookmark').then(bookmark => {
        if (bookmark && bookmark.position) {
            // 滚动到之前的位置
            window.scrollTo(0, bookmark.position);
        }
    }).catch(err => {
        console.error('读取书签失败:', err);
    });
}

// 获取当前位置的辅助函数
function getCurrentPosition() {
    return window.pageYOffset || document.documentElement.scrollTop;
}

// 添加滚动事件监听器，用于自动保存阅读进度
window.addEventListener('scroll', () => {
    // 可以设置节流来避免过于频繁的保存
    clearTimeout(scrollTimer);
    scrollTimer = setTimeout(save_bookmark, 1000); // 滚动停止1秒后保存
});

let scrollTimer;