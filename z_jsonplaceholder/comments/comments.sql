use test;

create table tbl_comments
(
    id      bigint auto_increment primary key,
    name    varchar(255) not null,
    email   varchar(255) not null,
    body    varchar(255) not null,
    post_id bigint       not null,
    constraint fk_comments_posts foreign key (post_id)
        references tbl_posts (id)
);
select *
from tbl_comments;


insert into tbl_comments(post_id, name, email, body)
values (1, 'id labore ex et quam laborum', 'Eliseo@gardner.biz',
        'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'),
       (2, 'quo vero reiciendis velit similique earum', 'Jayne_Kuhic@sydney.com',
        'est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et'),
       (3, 'odio adipisci rerum aut animi', 'Nikita@garfield.biz',
        'quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione'),
       (4, 'alias odio sit', 'Lew@alysha.tv',
        'non et atque\noccaecati deserunt quas accusantium unde odit nobis qui voluptatem\nquia voluptas consequuntur itaque dolor\net qui rerum deleniti ut occaecati'),
       (5, 'vero eaque aliquid doloribus et culpa', 'Hayden@althea.biz',
        'harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et'),
       (6, 'et fugit eligendi deleniti quidem qui sint nihil autem', 'Presley.Mueller@myrl.com',
        'doloribus at sed quis culpa deserunt consectetur qui praesentium\naccusamus fugiat dicta\nvoluptatem rerum ut voluptate autem\nvoluptatem repellendus aspernatur dolorem in'),
       (7, 'repellat consequatur praesentium vel minus molestias voluptatum', 'Dallas@ole.me',
        'maiores sed dolores similique labore et inventore et\nquasi temporibus esse sunt id et\neos voluptatem aliquam\naliquid ratione corporis molestiae mollitia quia et magnam dolor'),
       (8, 'et omnis dolorem', 'Mallory_Kunze@marie.org',
        'ut voluptatem corrupti velit\nad voluptatem maiores\net nisi velit vero accusamus maiores\nvoluptates quia aliquid ullam eaque'),
       (9, 'provident id voluptas', 'Meghan_Littel@rene.us',
        'sapiente assumenda molestiae atque\nadipisci laborum distinctio aperiam et ab ut omnis\net occaecati aspernatur odit sit rem expedita\nquas enim ipsam minus'),
       (10, 'eaque et deleniti atque tenetur ut quo ut', 'Carmen_Keeling@caroline.name',
        'voluptate iusto quis nobis reprehenderit ipsum amet nulla\nquia quas dolores velit et non\naut quia necessitatibus\nnostrum quaerat nulla et accusamus nisi facilis');
