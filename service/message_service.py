from model.message import Message

class MessageService:
    # TODO: Create message service with methods:
    # - send_to_user(cursor, message, username)
    # - get_all(cursor, username)
    # - find_by_id(cursor, message_id)
    # - find_by_recipient(cursor, recipient_username)

    @staticmethod
    def send_to_user(cursor, message, username):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE id=%s AND to_user=%s"
        ret = []
        cursor.execute(sql, (message, username,))
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message._id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.context = row[3]
            loaded_message.created_at = row[4]
            ret.append(loaded_message)
        return ret


    @staticmethod
    def get_all(cursor, username):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE from_user=%s"
        ret = []
        cursor.execute(sql, (username,))
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message._id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.context = row[3]
            loaded_message.created_at = row[4]
            ret.append(loaded_message)
        return ret

    @staticmethod
    def find_by_id(cursor, message_id):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE id=%s"
        ret = []
        cursor.execute(sql, (message_id,))
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message._id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.context = row[3]
            loaded_message.created_at = row[4]
            ret.append(loaded_message)
        return ret

    @staticmethod
    def find_by_recipient(cursor, recipient_username):
        sql = "SELECT id, from_user, to_user, context, created_at FROM messages WHERE to_user=%s"
        ret = []
        cursor.execute(sql, (recipient_username,))
        for row in cursor.fetchall():
            loaded_message = Message()
            loaded_message._id = row[0]
            loaded_message.from_user = row[1]
            loaded_message.to_user = row[2]
            loaded_message.context = row[3]
            loaded_message.created_at = row[4]
            ret.append(loaded_message)
        return ret

