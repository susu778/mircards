// 加载文本内容的函数，接受文件路径、目标元素ID和分组方式作为参数
function loadTextContent(file_path, target_element_id, groupBy) {
    // 创建 XMLHttpRequest 对象
    var xhr = new XMLHttpRequest();
    // 监听状态变化事件
    xhr.onreadystatechange = function() {
        // 当请求完成时
        if (xhr.readyState === XMLHttpRequest.DONE) {
            // 如果请求成功
            if (xhr.status === 200) {
                // 将响应文本按行拆分为数组
                var lines = xhr.responseText.split('\n');
                // 获取内容容器元素
                var contentContainer = document.getElementById(target_element_id);
                // 初始化用于存储分类的数组
                var enrichments = [];
                var categories = [];
                var mirnas = [];
                // 遍历每一行
                lines.forEach(function(line) {
                    // 将每行按制表符分割为富集方式、类别名和 MIRNA 名称
                    var [enrichment, category, ...mirna] = line.trim().split('\t');
                    // 将富集方式、类别名和 MIRNA 名称分别存储到对应数组中
                    enrichments.push(enrichment);
                    categories.push(category);
                    mirnas.push(...mirna);
                });
                // 对数组进行去重和排序
                enrichments = Array.from(new Set(enrichments)).sort();
                categories = Array.from(new Set(categories)).sort();
                mirnas = Array.from(new Set(mirnas)).sort();
                // 根据分组方式选择要显示的项目数组
                var items = groupBy === 'mirnas' ? mirnas : categories;
                // 渲染项目到内容容器中
                renderItems(items, contentContainer);
            }
        }
    };
    // 打开并发送 HTTP 请求
    xhr.open("GET", file_path, true);
    xhr.send();
}

// 渲染项目到指定容器的函数
function renderItems(items, contentContainer) {
    // 遍历项目数组
    items.forEach(function(element) {
        // 创建 div 元素
        var div = document.createElement("div");
        // 创建 span 元素，设置文本内容并绑定点击事件
        var span = document.createElement("span");
        span.textContent = element;
        span.onclick = function() {
            fillSearchBar(this.innerText);
        };
        // 将 span 元素添加到 div 元素中
        div.appendChild(span);
        // 将 div 元素添加到内容容器中
        contentContainer.appendChild(div);
    });
}
