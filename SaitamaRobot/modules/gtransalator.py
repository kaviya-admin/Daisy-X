 f r o m   e m o j i   i m p o r t   U N I C O D E _ E M O J I 
 f r o m   g o o g l e _ t r a n s _ n e w   i m p o r t   L A N G U A G E S ,   g o o g l e _ t r a n s l a t o r 
 f r o m   t e l e g r a m   i m p o r t   P a r s e M o d e ,   U p d a t e 
 f r o m   t e l e g r a m . e x t   i m p o r t   C a l l b a c k C o n t e x t ,   r u n _ a s y n c 
 
 f r o m   S a i t a m a R o b o t   i m p o r t   d i s p a t c h e r 
 f r o m   S a i t a m a R o b o t . m o d u l e s . d i s a b l e   i m p o r t   D i s a b l e A b l e C o m m a n d H a n d l e r 
 
 
 @ r u n _ a s y n c 
 d e f   t o t r a n s l a t e ( u p d a t e :   U p d a t e ,   c o n t e x t :   C a l l b a c k C o n t e x t ) : 
         m e s s a g e   =   u p d a t e . e f f e c t i v e _ m e s s a g e 
         p r o b l e m _ l a n g _ c o d e   =   [ ] 
         f o r   k e y   i n   L A N G U A G E S : 
                 i f   " - "   i n   k e y : 
                         p r o b l e m _ l a n g _ c o d e . a p p e n d ( k e y ) 
 
         t r y : 
                 i f   m e s s a g e . r e p l y _ t o _ m e s s a g e : 
                         a r g s   =   u p d a t e . e f f e c t i v e _ m e s s a g e . t e x t . s p l i t ( N o n e ,   1 ) 
                         i f   m e s s a g e . r e p l y _ t o _ m e s s a g e . t e x t : 
                                 t e x t   =   m e s s a g e . r e p l y _ t o _ m e s s a g e . t e x t 
                         e l i f   m e s s a g e . r e p l y _ t o _ m e s s a g e . c a p t i o n : 
                                 t e x t   =   m e s s a g e . r e p l y _ t o _ m e s s a g e . c a p t i o n 
 
                         t r y : 
                                 s o u r c e _ l a n g   =   a r g s [ 1 ] . s p l i t ( N o n e ,   1 ) [ 0 ] 
                         e x c e p t   ( I n d e x E r r o r ,   A t t r i b u t e E r r o r ) : 
                                 s o u r c e _ l a n g   =   " e n " 
 
                 e l s e : 
                         a r g s   =   u p d a t e . e f f e c t i v e _ m e s s a g e . t e x t . s p l i t ( N o n e ,   2 ) 
                         t e x t   =   a r g s [ 2 ] 
                         s o u r c e _ l a n g   =   a r g s [ 1 ] 
 
                 i f   s o u r c e _ l a n g . c o u n t ( ' - ' )   = =   2 : 
                         f o r   l a n g   i n   p r o b l e m _ l a n g _ c o d e : 
                                 i f   l a n g   i n   s o u r c e _ l a n g : 
                                         i f   s o u r c e _ l a n g . s t a r t s w i t h ( l a n g ) : 
                                                 d e s t _ l a n g   =   s o u r c e _ l a n g . r s p l i t ( " - " ,   1 ) [ 1 ] 
                                                 s o u r c e _ l a n g   =   s o u r c e _ l a n g . r s p l i t ( " - " ,   1 ) [ 0 ] 
                                         e l s e : 
                                                 d e s t _ l a n g   =   s o u r c e _ l a n g . s p l i t ( " - " ,   1 ) [ 1 ] 
                                                 s o u r c e _ l a n g   =   s o u r c e _ l a n g . s p l i t ( " - " ,   1 ) [ 0 ] 
                 e l i f   s o u r c e _ l a n g . c o u n t ( ' - ' )   = =   1 : 
                         f o r   l a n g   i n   p r o b l e m _ l a n g _ c o d e : 
                                 i f   l a n g   i n   s o u r c e _ l a n g : 
                                         d e s t _ l a n g   =   s o u r c e _ l a n g 
                                         s o u r c e _ l a n g   =   N o n e 
                                         b r e a k 
                         i f   d e s t _ l a n g   i s   N o n e : 
                                 d e s t _ l a n g   =   s o u r c e _ l a n g . s p l i t ( " - " ) [ 1 ] 
                                 s o u r c e _ l a n g   =   s o u r c e _ l a n g . s p l i t ( " - " ) [ 0 ] 
                 e l s e : 
                         d e s t _ l a n g   =   s o u r c e _ l a n g 
                         s o u r c e _ l a n g   =   N o n e 
 
                 e x c l u d e _ l i s t   =   U N I C O D E _ E M O J I . k e y s ( ) 
                 f o r   e m o j i   i n   e x c l u d e _ l i s t : 
                         i f   e m o j i   i n   t e x t : 
                                 t e x t   =   t e x t . r e p l a c e ( e m o j i ,   ' ' ) 
 
                 t r l   =   g o o g l e _ t r a n s l a t o r ( ) 
                 i f   s o u r c e _ l a n g   i s   N o n e : 
                         d e t e c t i o n   =   t r l . d e t e c t ( t e x t ) 
                         t r a n s _ s t r   =   t r l . t r a n s l a t e ( t e x t ,   l a n g _ t g t = d e s t _ l a n g ) 
                         r e t u r n   m e s s a g e . r e p l y _ t e x t ( 
                                 f " T r a n s l a t e d   f r o m   ` { d e t e c t i o n [ 0 ] } `   t o   ` { d e s t _ l a n g } ` : \ n ` { t r a n s _ s t r } ` " , 
                                 p a r s e _ m o d e = P a r s e M o d e . M A R K D O W N ) 
                 e l s e : 
                         t r a n s _ s t r   =   t r l . t r a n s l a t e ( 
                                 t e x t ,   l a n g _ t g t = d e s t _ l a n g ,   l a n g _ s r c = s o u r c e _ l a n g ) 
                         m e s s a g e . r e p l y _ t e x t ( 
                                 f " T r a n s l a t e d   f r o m   ` { s o u r c e _ l a n g } `   t o   ` { d e s t _ l a n g } ` : \ n ` { t r a n s _ s t r } ` " , 
                                 p a r s e _ m o d e = P a r s e M o d e . M A R K D O W N ) 
 
         e x c e p t   I n d e x E r r o r : 
                 u p d a t e . e f f e c t i v e _ m e s s a g e . r e p l y _ t e x t ( 
                         " R e p l y   t o   m e s s a g e s   o r   w r i t e   m e s s a g e s   f r o m   o t h e r   l a n g u a g e s     f o r   t r a n s l a t i n g   i n t o   t h e   i n t e n d e d   l a n g u a g e \ n \ n " 
                         " E x a m p l e :   ` / t r   e n - m l `   t o   t r a n s l a t e   f r o m   E n g l i s h   t o   M a l a y a l a m \ n " 
                         " O r   u s e :   ` / t r   m l `   f o r   a u t o m a t i c   d e t e c t i o n   a n d   t r a n s l a t i n g   i t   i n t o   M a l a y a l a m . \ n " 
                         " S e e   [ L i s t   o f   L a n g u a g e   C o d e s ] ( t . m e / O n e P u n c h S u p p o r t / 1 2 8 2 3 )   f o r   a   l i s t   o f   l a n g u a g e   c o d e s . " , 
                         p a r s e _ m o d e = " m a r k d o w n " , 
                         d i s a b l e _ w e b _ p a g e _ p r e v i e w = T r u e ) 
         e x c e p t   V a l u e E r r o r : 
                 u p d a t e . e f f e c t i v e _ m e s s a g e . r e p l y _ t e x t ( 
                         " T h e   i n t e n d e d   l a n g u a g e   i s   n o t   f o u n d ! " ) 
         e l s e : 
                 r e t u r n 
 
 
 _ _ h e l p _ _   =   " " " 
 "   ` / t r `   o r   ` / t l `   ( l a n g u a g e   c o d e )   a s   r e p l y   t o   a   l o n g   m e s s a g e 
 * E x a m p l e : *   
     ` / t r   e n ` * : *   t r a n s l a t e s   s o m e t h i n g   t o   e n g l i s h 
     ` / t r   h i - e n ` * : *   t r a n s l a t e s   h i n d i   t o   e n g l i s h 
 " " " 
 
 T R A N S L A T E _ H A N D L E R   =   D i s a b l e A b l e C o m m a n d H a n d l e r ( [ " t r " ,   " t l " ] ,   t o t r a n s l a t e ) 
 
 d i s p a t c h e r . a d d _ h a n d l e r ( T R A N S L A T E _ H A N D L E R ) 
 
 _ _ m o d _ n a m e _ _   =   " T r a n s l a t o r " 
 _ _ c o m m a n d _ l i s t _ _   =   [ " t r " ,   " t l " ] 
 _ _ h a n d l e r s _ _   =   [ T R A N S L A T E _ H A N D L E R ]