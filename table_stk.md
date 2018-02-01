meetyou数据库表结构

表 letter

| 字段          | 类型        | 说明                 |
| ----------- | --------- | ------------------ |
| id          | 自增长主键     |                    |
| user_id     | int       | 信件所属人id（值为0时为推荐信件） |
| user_letter | text      | 用户所写的信件            |
| send_time   | timestamp | 发送时间               |
| to_user_id  | int       | 发送用户id             |
|             |           |                    |
|             |           |                    |

表 record

| 字段         | 类型           | 说明     |
| ---------- | ------------ | ------ |
| id         | 子增长主键        |        |
| letter_id  | int          | 录音随信id |
| record_url | varchar(200) | 录音保存地址 |

