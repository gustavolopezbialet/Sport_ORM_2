from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		#"baseball_leagues": League.objects.filter(sport="Baseball"),
		"baseball_leagues": League.objects.filter(sport__contains="baseball"),
		"women_leagues": League.objects.filter(name__contains="women"),
		"all_hockey_leagues": League.objects.filter(sport__contains="hockey"),
		"not_football_leagues": League.objects.exclude(sport__contains="football"),
		"conferences_leagues": League.objects.filter(name__contains="conference"),
		"all_league_atlantic": League.objects.filter(name__contains="atlantic"),
		"teams_house_dallas": Team.objects.filter(location__contains="dallas"),
		"teams_with_raptors": Team.objects.filter(team_name__contains="raptors"),
		"teams_with_city": Team.objects.filter(location__contains="city"),
		"teams_startswith_t": Team.objects.filter(team_name__startswith="T"),
		"teams_orderby_location": Team.objects.all().order_by("location"),
		"teams_orderby_name": Team.objects.all().order_by("-team_name"),
		"player_lastname_cooper": Player.objects.filter(last_name__contains="cooper"),
		"player_name_joshua": Player.objects.filter(first_name__contains="joshua"),
		"player_cooper_less_joshua": Player.objects.filter(last_name__contains="cooper").exclude(first_name__contains="joshua"),
		"player_name_alexander_or_wyatt": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),
	}
	return render(request, "leagues/index.html", context)

def index2(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"teams_atlantic_soccer_conference": Team.objects.filter(league__name__contains="atlantic soccer conference"),
	}
	return render(request, "leagues/index2.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")