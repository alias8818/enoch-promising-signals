# Evidence-ledger rollback for tool-using small agent reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-rollback-for-tool-using-small-agent-reliability-0fd30414bbbd`
Run ID: `evidence-ledger-rollback-for-tool-using-small-agent-reliability-0fd30414bbbd-20260609T035255396154+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ed565345b183

## What looked useful

At 30% observation corruption, stale-cache baseline success was 0.8960 while ledger rollback and refresh control both reached 0.9965. Ledger beat stale cache across nonzero corruption settings but had zero paired success discordance versus refresh control at all settings.

## Boundaries and scale limits

2,000 paired synthetic tasks per corruption setting; no real LLM, natural-language tool use, production API failures, or multi-hop dependency graph; CPU-only run completed in under one second.

## Claim scope

In a deterministic synthetic catalog-selection tool-agent benchmark with transient observation corruption and stochastic small-agent selection slips, invalidating stale evidence after verifier contradiction improves reliability over a stale-cache baseline, but evidence-ledger rollback provides no advantage over a simpler clear-cache-on-failure control.

## Why it stopped

Proxy/local result: useful early evidence for stale-evidence invalidation, but not a full validation and not supportive of ledger-specific advantage in the tested simple setting.

## Recommended next action

Run a bounded multi-hop dependency benchmark where selective ledger rollback can be compared against full cache refresh on both success and tool-call cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Selective rollback versus full refresh in multi-hop tool-agent tasks
- Success threshold: Selective ledger rollback matches full-refresh success within 1 percentage point while reducing mean tool calls by at least 15%, or exceeds full-refresh success when both use the same retry/tool-call budget.
- Stop condition: Stop if selective rollback has no success or tool-call advantage over full refresh across the tested corruption rates with at least 2,000 paired tasks per setting.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-rollback-for-tool-using-small-agent-reliability-0fd30414bbbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
