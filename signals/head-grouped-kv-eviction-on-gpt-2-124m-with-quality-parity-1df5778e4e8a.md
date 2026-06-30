# Head-Grouped KV Eviction on GPT-2-124M with Quality Parity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `head-grouped-kv-eviction-on-gpt-2-124m-with-quality-parity-1df5778e4e8a`
Run ID: `head-grouped-kv-eviction-on-gpt-2-124m-with-quality-parity-1df5778e4e8a-20260619T063159335718+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cfd9f4a57e07

## What looked useful

Head grouping reduced delta NLL versus uniform at equal max effective KV tokens for budget 96 (0.049193 to 0.040181) and budget 64 (0.145373 to 0.124174), but all eviction strategies failed quality parity.

## Boundaries and scale limits

CPU-only short-context run on a small local text corpus; no optimized serving kernel, no standard benchmark corpus, no long-context evaluation, no generated-text human quality assessment, and no models larger than GPT-2-small.

## Claim scope

On a 160-token local GPT-2-small direct next-token NLL probe, deterministic head-grouped KV eviction modestly improves over uniform sink-plus-recent eviction at average per-head budgets 64 and 96, but does not meet the predefined quality parity threshold of delta NLL <= 0.02 versus full context.

## Why it stopped

Direct bounded GPT-2-small evidence failed the quality parity threshold; this is an early scoped falsification of the tested deterministic head-grouped eviction rule, not a full long-context validation.

## Recommended next action

Stop this run as no-paper useful-signal evidence; a separate bounded follow-up should test a learned or attention-mass-selected grouped retention policy on a standard corpus before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard-corpus GPT-2 head-grouped KV eviction with learned retention thresholds
- Success threshold: Grouped eviction achieves delta NLL <= 0.02 versus full context and beats matched-budget uniform eviction by at least 0.01 NLL while reducing effective KV tokens by at least 25%.
- Stop condition: Stop if matched-budget grouped eviction remains above delta NLL 0.02 on the first standard-corpus medium probe or fails to beat uniform eviction by at least 0.01 NLL.

## Evidence references

- Artifact root: `<local-path>/projects/head-grouped-kv-eviction-on-gpt-2-124m-with-quality-parity-1df5778e4e8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
