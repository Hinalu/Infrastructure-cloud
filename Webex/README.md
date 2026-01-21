# Webex Automation

## Tasks Overview
Webex Teams API interaction (Criteria W1, W2).

### Included Files
* **`W2_manage_spaces.py`**: Creates, posts to, and deletes a room.

---

## 🎓 Exam Prep: Concepts & Explanations

### 1. What is ChatOps?
Using chat platforms (like Webex or Slack) to perform operations. Instead of opening a dashboard, a bot sends you an alert, or you type a command to a bot to restart a server.

### 2. The Logic Flow
1. **Create Room:** Returns a `roomId`. We *must* save this ID.
2. **Post Message:** We use that saved `roomId` to tell Webex *where* to post the message.
3. **Delete:** We use the `roomId` again to identify which room to destroy.