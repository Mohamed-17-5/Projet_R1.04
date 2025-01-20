<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Attribute\Route;

class LoisirController extends AbstractController
{
    #[Route('/loisir', name: 'app_loisir')]
    public function index(): Response
    {
        return $this->render('loisir/index.html.twig', [
            'controller_name' => 'LoisirController',
        ]);
    }
}