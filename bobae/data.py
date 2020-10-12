
class Board:
    title = None
    writer = None
    date = None
    like = None
    hit = None
    content = None
    images = None
    replies = None

    def __str__(self):
        out = ''
        out += 'title: ' + self.title
        out += '\nwriter: {}\ndate: {}\nlike: {}\nhit: {}\n'.format(self.writer, self.date, self.like, self.hit)
        out += 'content: ' + self.content

        out += '\n[reply]\n'
        for reply in self.replies:
            out += 'writer: {}\ndate: {}\n'.format(reply.writer, reply.date)
            out += 'content: ' + reply.content
            out += '\n'

        return out


class Reply:
    content = None
    writer = None
    date = None
