from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models import Player, Ban, Card, PlayerCard


class BanInline(admin.TabularInline):
    model = Ban
    fk_name = "player"
    extra = 1


class PlayerCardInline(admin.TabularInline):
    model = PlayerCard
    extra = 1


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["username", "discord_id", "date_joined", "is_staff", "permanent_ban"]
    list_filter = ["date_joined", "is_staff", "permanent_ban"]
    inlines = [BanInline, PlayerCardInline]
    search_fields = ["username", "discord_id"]
    actions = ["permanently_ban", "permanently_unban"]
    fieldsets = [
        [None, {"fields": ["username", "password", "coins", "permanent_ban"]}],
        ["Personal info", {"fields": ["email", "discord_id"]}],
        [
            "Permissions",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ],
            },
        ],
        ["Important dates", {"fields": ["last_login", "date_joined"]}],
    ]

    @admin.action(description="Permanently ban selected players")
    def permanently_ban(self, request, queryset):
        updated = queryset.update(permanent_ban=True)
        self.message_user(
            request,
            ngettext(
                "%d player was successfully banned permanently.",
                "%d players were successfully banned permanently.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )

    @admin.action(description="Permanently unban selected players")
    def permanently_unban(self, request, queryset):
        updated = queryset.update(permanent_ban=False)
        self.message_user(
            request,
            ngettext(
                "%d player was successfully unbanned permanently.",
                "%d players were successfully unbanned permanently.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ["id", "color", "element", "power", "value"]
    list_filter = ["color", "element", "power", "value"]
    search_fields = ["id"]


@admin.register(Ban)
class CardAdmin(admin.ModelAdmin):
    list_display = ["player", "issued", "expires", "moderator"]
    list_filter = ["player", "issued", "expires", "moderator"]
    search_fields = ["player"]


admin.site.register(PlayerCard)
