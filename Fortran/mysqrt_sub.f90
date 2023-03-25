program mysqrt_sub
        implicit none
        real(kind=8) :: x,y,sqrt_true,sqrt_NT,s_init,tol
        integer :: kmax, k
        x=2.d0
        kmax=100
        s_init=1.d0
        tol=1.d-14
        sqrt_true=sqrt(x)
        call sqrtNT_sub(x,kmax,tol,s_init,sqrt_NT,k)
        !y=sqrt_NT(x)
        print *, "x= ",x
        print *, "sqrt_true= ",sqrt_true
        print *, "sqrtNT= ",sqrt_NT
        print *, "error= ", sqrt_true-sqrt_NT
        print *, "k= ", k

end program mysqrt_sub

subroutine sqrtNT_sub(x,kmax,tol,s_init,sqrtNT,k)
        implicit none
        
        !subroutine arguments
        real(kind=8), intent(in) :: x, s_init, tol
        integer, intent(in) ::  kmax
        real(kind=8), intent(out) :: sqrtNT
        integer, intent(out) :: k
        
        !local variable
        real(kind=8) :: s_prev, delta_s, s
        !integer :: k
        
        s=s_init

        do k=1,kmax
                s_prev=s
                s=0.5*(s+x/s)
                delta_s=s-s_prev
                if ((delta_s/x)<tol) then
                        exit
                end if
        end do
        
        !print *, "k=",k
        if (k>=kmax) then
                print *, "Newton Method to find out square root of a number did not converge"
        end if

        sqrtNT=s

end subroutine sqrtNT_sub
