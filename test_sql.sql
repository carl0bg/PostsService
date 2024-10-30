select*from posts;

select p.user_id, u.username, p.id, ph.file, v.id from posts p left join photo ph on p.id = ph.post_id
 left join users u on p.user_id = u.id
 left join video v on p.id = v.post_id;