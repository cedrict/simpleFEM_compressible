subroutine compute_derivatives_errors(nel,np,x,y,dxu_nodal, dxv_nodal, dyu_nodal, dyv_nodal, phi_nodal,icon,ibench,dxu_L1, dxu_L2, dxv_L1, dxv_L2, dyu_L1, dyu_L2, dyv_L1, dyv_L2,phi_L1,phi_L2)

implicit none

integer, parameter :: m=4
integer nel,np,ibench
integer icon(4,nel)
real(8) x(np),y(np)
real(8) dxu_L1,dxu_L2,dxv_L1,dxv_L2,dyu_L1,dyu_L2,dyv_L1,dyv_L2,phi_L1,phi_L2
real(8) dxu_nodal(np),dxv_nodal(np),dyu_nodal(np),dyv_nodal(np),phi_nodal(np)
real(8), external ::  e_xx,e_yy,e_xy,phi
real(8) xq,yq,uq,vq,jcb(2,2)  
integer iel,k,iq,jq
real(8) N(m),dNdx(m),dNdy(m),dNdr(m),dNds(m)
real(8) rq,sq,wq,vthq,uthq,pthq,pq,jcob
real(8) dudxq,dvdxq,dudyq,dvdyq

dxu_L1=0
dxu_L2=0
dxv_L1=0
dxv_L2=0
dyu_L1=0
dyu_L2=0
dyv_L1=0
dyv_L2=0
phi_L1=0
phi_L2=0

do iel=1,nel

   do iq=-1,1,2
   do jq=-1,1,2

      rq=iq/sqrt(3.d0)
      sq=jq/sqrt(3.d0)
      wq=1.d0*1.d0

      N(1)=0.25d0*(1.d0-rq)*(1.d0-sq)
      N(2)=0.25d0*(1.d0+rq)*(1.d0-sq)
      N(3)=0.25d0*(1.d0+rq)*(1.d0+sq)
      N(4)=0.25d0*(1.d0-rq)*(1.d0+sq)

      dNdr(1)= - 0.25d0*(1.d0-sq)   ;   dNds(1)= - 0.25d0*(1.d0-rq)
      dNdr(2)= + 0.25d0*(1.d0-sq)   ;   dNds(2)= - 0.25d0*(1.d0+rq)
      dNdr(3)= + 0.25d0*(1.d0+sq)   ;   dNds(3)= + 0.25d0*(1.d0+rq)
      dNdr(4)= - 0.25d0*(1.d0+sq)   ;   dNds(4)= + 0.25d0*(1.d0-rq)

      jcb=0.d0
      do k=1,m
         jcb(1,1)=jcb(1,1)+dNdr(k)*x(icon(k,iel))
         jcb(1,2)=jcb(1,2)+dNdr(k)*y(icon(k,iel))
         jcb(2,1)=jcb(2,1)+dNds(k)*x(icon(k,iel))
         jcb(2,2)=jcb(2,2)+dNds(k)*y(icon(k,iel))
      enddo

      jcob=jcb(1,1)*jcb(2,2)-jcb(2,1)*jcb(1,2)

      xq=0
      yq=0
      dudxq=0
      dudyq=0
      dvdxq=0
      dvdyq=0
      do k=1,m
         xq=xq+N(k)*x(icon(k,iel))
         yq=yq+N(k)*y(icon(k,iel))
         dudxq=dudxq+N(k)*dxu_nodal(icon(k,iel))
         dudyq=dudyq+N(k)*dyu_nodal(icon(k,iel))
         dvdxq=dvdxq+N(k)*dxv_nodal(icon(k,iel))
         dvdyq=dvdyq+N(k)*dyv_nodal(icon(k,iel))
      end do

      dxu_L1 = dxu_L1 + abs(dudxq-e_xx(xq,yq,ibench))   *jcob*wq
      dxu_L2 = dxu_L2 +    (dudxq-e_xx(xq,yq,ibench))**2*jcob*wq

      dyu_L1 = dyu_L1 + abs(dudyq-e_xy(xq,yq,ibench))   *jcob*wq
      dyu_L2 = dyu_L2 +    (dudyq-e_xy(xq,yq,ibench))**2*jcob*wq

      dxv_L1 = dxv_L1 + abs(dvdxq-e_xy(xq,yq,ibench))   *jcob*wq
      dxv_L2 = dxv_L2 +    (dvdxq-e_xy(xq,yq,ibench))**2*jcob*wq

      dyv_L1 = dyv_L1 + abs(dvdyq-e_yy(xq,yq,ibench))   *jcob*wq
      dyv_L2 = dyv_L2 +    (dvdyq-e_yy(xq,yq,ibench))**2*jcob*wq

      !phi_L1 = phi_L1 + abs(phi_nodal(i)-phi(xq,yq,ibench))*jcob*wq
      !phi_L2 = phi_L2 + (phi_nodal(i)-phi(xq,yq,ibench))**2*jcob*wq

   end do
   end do

end do

dxu_L2 = sqrt(dxu_L2)
dxv_L2 = sqrt(dxv_L2)
dyu_L2 = sqrt(dyu_L2)
dyv_L2 = sqrt(dyv_L2)
phi_L2 = sqrt(phi_L2)

end subroutine
