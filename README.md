# 🚀 Industrial IoT Sorting System – AWS Based Project
 
This is a demonstration project simulating a smart industrial sorting system using ESP32, AWS, and a responsive web interface. It showcases real-time data monitoring and control using modern IoT and cloud tools.

## 🧠 Project Overview

- A smart, cloud-connected sorting system where:

- The ESP32 collects sensor and system data

- Data is sent to AWS DynamoDB via REST APIs

- A web dashboard (hosted on AWS S3) provides real-time monitoring and data entry

## 📋 Process Flow

🔧 Step 1: Setup ESP32 to Collect and Send Data
🖥️ Code the ESP32 using Arduino IDE

📡 Connect to Wi-Fi

🌡️ Collect real-time temperature and humidity data

📦 Package data in JSON format

🔐 Send data securely via HTTPS POST to AWS API Gateway

## ☁️ Step 2: Build the AWS Backend Infrastructure

🔗 API Gateway

- Create REST API with multiple endpoints (POST/GET)

- Enable CORS for cross-origin access

### 🧠 Lambda Functions

- Handle logic for storing and retrieving data

- Serialize data (e.g., convert Decimal to float for JSON)

* Test Case: Insert Web Data (POST)

```
{
  "httpMethod": "POST",
  "body": "{\"source\":\"web\",\"item\":\"apple\",\"count\":10,\"machine\":\"on\",\"motor\":\"off\"}"
}

```
* Test Case: Insert ESP32 Data (POST)

 ```
{
  "httpMethod": "POST",
  "body": "{\"source\":\"esp\",\"temperature\":28.4,\"humidity\":65.1}"
}
```

* Test cases for Read data

```
{
  "httpMethod": "GET",
  "queryStringParameters": {
    "type": "web"
  }
}
```

### 🗃️ DynamoDB Tables

Table 1: SortingSystem – item type, count, motor/machine states

Table 2: SensorData – temperature, humidity with timestamps

## 🌐 Step 3: Develop the Web Dashboard (Frontend)

🛠️ Build two HTML pages:

- Insert.html: Manual data entry (item, count, state)

- Monitor.html: Real-time data display

🔄 Use JavaScript fetch() to call API Gateway endpoints

🎨 Add responsive styling with HTML + CSS

## ☁️ Step 4: Host Frontend on AWS S3

🪣 Create an S3 bucket

📁 Upload HTML, CSS, JS files

🌍 Enable static website hosting

🔧 Set index.html as the default page

#### Bucket Permision add

* Amazon S3 < General purpose buckets < Permissions

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::web-sorting-system/*"
        }
    ]
```
* Static website hosting - Enable

##Additional - Basic Permissions policies

* I AM < Role < role_name - AmazonDynamoDBFullAccess , AWSLambdaBasicExecutionRole
                        

## ✅ Step 5: Testing and Demonstration

🔌 Power up ESP32 and confirm data is sent to AWS

👀 Open the web dashboard to:

- View real-time sensor data

- Monitor sorting system status

- Insert manual entries and see them reflected instantly

## 🎯 Final Outcome

- A fully working proof-of-concept smart sorting system showing:

- Real-time IoT data collection

- Cloud processing and storage

- Web-based visualization and control

