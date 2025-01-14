<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class SeydinaController extends AbstractController
{
    #[Route('/seydina', name: 'app_seydina')]
    public function index(): Response
    {
        return $this->render('seydina/index.html.twig', [
            'controller_name' => 'SeydinaController',
        ]);
    }

    #[Route('/blog/home', name: 'app_home')]
    public function home(): Response
    {
        return $this->render('seydina/home.html.twig');
    }
}


