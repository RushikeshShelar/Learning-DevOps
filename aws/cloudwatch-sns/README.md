# 📊 AWS CloudWatch & 📣 SNS (Simple Notification Service)

---

## 🕵️‍♂️ What is Amazon CloudWatch?

**Amazon CloudWatch** is a monitoring and observability service that provides data and actionable insights for AWS resources, applications, and services running on AWS or on-premises. It helps you **collect logs, monitor metrics**, set up **alarms**, and **automate responses** to changes in your infrastructure.

CloudWatch is often referred to as the "eyes and ears" of AWS infrastructure. It's widely used for tracking performance, resource utilization, operational health, and debugging issues across your AWS ecosystem.

---

## 📏 CloudWatch Metrics

**Metrics** are the fundamental concept in CloudWatch. They are time-ordered sets of data points that represent a measurable characteristic of your resource or application (like CPU usage, memory, disk I/O, etc.).

CloudWatch collects:

- **Default metrics** for AWS services (e.g., EC2 CPU utilization, S3 request counts, RDS storage usage).
- **Custom metrics** that you can push yourself using AWS CLI, SDK, or from your application.

### Example: Default Metric
EC2 instances automatically publish CPU utilization under:
```
Namespace: AWS/EC2
Metric Name: CPUUtilization
Dimensions: InstanceId=i-xxxxxxxxxxxxx
```

### Creating Custom Metrics:
You can publish custom metrics using the AWS CLI or SDK:
```bash
aws cloudwatch put-metric-data \
  --namespace "CustomApp" \
  --metric-name "ActiveUsers" \
  --value 150 \
  --dimensions "Service=LoginAPI"
```

Custom metrics are useful when you're monitoring application-specific events like:
- Number of signups per minute
- Failed login attempts
- Queue depth

---

## 🔔 CloudWatch Alarms

**Alarms** are used to watch a single metric or a math expression and perform actions based on the value. When a metric crosses a specified threshold, the alarm state changes and triggers actions (like notifications, auto-scaling, recovery, etc.).

There are three states of an alarm:
- `OK`: Everything is within the threshold.
- `ALARM`: The metric breached the defined threshold.
- `INSUFFICIENT_DATA`: Not enough data is available.

### Example Use-Case:
You can set an alarm to monitor CPU usage of an EC2 instance and notify you via SMS if it exceeds 80% for 5 minutes.

**Alarm Configuration:**
- Metric: `CPUUtilization`
- Threshold: > 80%
- Period: 300 seconds
- Evaluation periods: 1
- Action: Notify via SNS topic

This allows automated responses like:
- Sending alerts
- Auto-restarting instances
- Triggering Lambda functions

---

## 📁 CloudWatch Logs

**CloudWatch Logs** let you collect and monitor **log files** from EC2 instances, Lambda functions, and other AWS services or custom applications.

Each log stream is grouped into a **Log Group**. You can filter logs, set retention policies, and even trigger metric filters or alarms from logs.

### Example: Logging from EC2
Install and configure the CloudWatch agent to push logs from EC2:
```bash
sudo yum install amazon-cloudwatch-agent
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a start
```

You can stream logs like:
- `/var/log/messages`
- `/var/log/nginx/access.log`

Once the logs are in CloudWatch, you can use **Log Insights** to run SQL-like queries for analysis.

---

## 📣 Amazon SNS – Simple Notification Service

**Amazon SNS (Simple Notification Service)** is a fully managed pub/sub (publish-subscribe) messaging service. It allows you to **send messages or alerts** to multiple subscribers (like email, SMS, Lambda, or HTTP endpoints) through **topics**.

---

## 🧵 Topics and Subscriptions

### Topics:
A **topic** is a communication channel. When a message is published to a topic, all its subscribers receive the message.

### Subscriptions:
Subscribers can choose different protocols:
- Email
- SMS
- AWS Lambda
- HTTP/HTTPS endpoints
- SQS queues

For example, a CloudWatch alarm can publish a message to an SNS topic when CPU usage is high, and SNS can then send that message to multiple subscribers (developers via email and on-call via SMS).

---

### Example Flow:

1. Create an SNS Topic:
```bash
aws sns create-topic --name cpu-alerts
```

2. Subscribe your phone number:
```bash
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:111122223333:cpu-alerts \
  --protocol sms \
  --notification-endpoint "+919999999999"
```

3. In CloudWatch, set alarm action to publish to this SNS topic.

Now whenever the alarm triggers, all subscribers (e.g., SMS/email) are instantly notified.

> 📦 SNS is **highly scalable** and supports **millions of messages per second**.

---

## 🚨 Practical Scenario

You're running a web app on EC2. You want to:
- Get notified if the app crashes or uses too much CPU.
- Debug logs when error spikes happen.

**Solution:**
- Use CloudWatch to collect logs and monitor metrics.
- Set alarms on metrics like `CPUUtilization` and `StatusCheckFailed`.
- Create an SNS topic, add your email and phone number as subscribers.
- Link the alarm to the SNS topic.
- If threshold is crossed, CloudWatch triggers the alarm → SNS sends notification → You get notified in real-time.

---

> ✅ With CloudWatch and SNS combined, you build a complete monitoring and alerting pipeline for your infrastructure and applications.

---