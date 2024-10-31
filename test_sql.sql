select*from posts;

select p.user_id, u.username, p.id, ph.file, v.id from posts p left join photo ph on p.id = ph.post_id
 left join users u on p.user_id = u.id
 left join video v on p.id = v.post_id;



-- select pp.* from product_photo pp left join product p on p.id = pp.product_id where p.id = 2;

-- -- insert into product_photo (url, product_id) VALUES ('s;lds;ad;ad.ru', 2);


-- select pp.url, p.* from product_photo pp inner join product p on p.id = pp.product_id;

-- INSERT into cart_product(cart_id, product_id) VALUES (1, 2);

-- delete from cart_product where cart_id = 2;


-- select c.name, p.price from customer c left join cart on cart.customer_id = c.id left join cart_product cp on cp.cart_id = cart.id left join product p on p.id = p.id GROUP BY c.name;
-- #сделать к плюсом к выводу еще общий прайс #доделать



