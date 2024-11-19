<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coin Tools</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .sidebar {
            width: 250px;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            position: fixed;
            height: 100vh;
        }

        .main-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #1e88e5;
        }

        .menu-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .menu-item {
            padding: 12px 16px;
            margin-bottom: 8px;
            cursor: pointer;
            border-radius: 6px;
            transition: background-color 0.3s;
        }

        .menu-item:hover {
            background-color: #f0f7ff;
        }

        .menu-item.active {
            background-color: #e3f2fd;
            color: #1e88e5;
            font-weight: bold;
        }

        .content {
            margin-left: 270px;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .calculator-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .input-section {
            margin-top: 20px;
        }

        .input-label {
            display: block;
            margin-bottom: 10px;
            color: #666;
        }

        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }

        input[type="url"] {
            flex: 1;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
        }

        .submit-btn {
            padding: 12px 24px;
            background-color: #1e88e5;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #1976d2;
        }

        .stats-section {
            margin-top: 30px;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            <div class="main-title">Coin Tools</div>
            <ul class="menu-list">
                <li class="menu-item active">Bybit LaunchPool Calculator</li>
                <li class="menu-item">Smart Arbitrage</li>
                <li class="menu-item">Bitcoin DCA Calculator</li>
            </ul>
        </div>

        <div class="content">
            <div class="calculator-title">Bybit LaunchPool Calculator</div>
            
            <div class="input-section">
                <label class="input-label">Enter Bybit Announcement URL</label>
                <div class="input-group">
                    <input type="url" id="urlInput" placeholder="https://announcements.bybit.com/...">
                    <button class="submit-btn" onclick="submitUrl()">Submit</button>
                </div>
            </div>

            <div class="stats-section">
                <div class="calculator-title">Calculator Stats</div>
                <!-- 这里可以添加统计信息 -->
            </div>
        </div>
    </div>

    <script>
        function submitUrl() {
            const url = document.getElementById('urlInput').value;
            if (url) {
                // 这里可以添加URL验证逻辑
                window.location.href = url;
            } else {
                alert('Please enter a valid URL');
            }
        }
    </script>
</body>
</html> 