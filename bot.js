const TeleBot = require('telebot');
const bot = new TeleBot('466035657:AAEvvOBlKMdcxqg7IDnngnHC2vRbc2qAkbM');

//bot.on('text', (msg) => msg.reply.text(msg.text));
bot.on('sticker', (msg) => {
    return msg.reply.sticker("You just sent a sticker, wow!", { asReply: true });
});
bot.on(['/start', '/hello'], (msg) => msg.reply.text('Welcome!'));

bot.start();



