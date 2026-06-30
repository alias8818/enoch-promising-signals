# DataMix ratio sweep for GPT-2-tiny on gb10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `datamix-ratio-sweep-for-gpt-2-tiny-on-gb10-b9fd866c7633`
Run ID: `datamix-ratio-sweep-for-gpt-2-tiny-on-gb10-b9fd866c7633-20260620T010135205971+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/c78037a2cdbf

## What looked useful

Endpoint-only mixtures specialize and fail on the omitted domain, while mixed ratios sharply reduce held-out loss. Across three seeds, ratio A=0.50 had aggregate mean loss 2.6265 and worst-domain loss 2.6992, versus endpoint mean losses 5.1216 and 5.5835.

## Boundaries and scale limits

The result uses an 834,304-parameter GPT-2-like model, synthetic token-transition data, 180 training steps per ratio, three seeds, and equal-weighted synthetic validation domains. It does not validate natural-language or code pretraining, tokenizer effects, longer convergence, or GPT-2-small-class scaling.

## Claim scope

On two deterministic synthetic domains, a GPT-2-tiny style causal decoder trained from scratch for fixed tokens shows a reproducible data-mix tradeoff; the 50/50 mixture gives the best three-seed aggregate mean and worst-domain validation loss.

## Why it stopped

This run produced a reproducible synthetic useful signal, but the evidence is not broad or direct enough for a paper-grade DataMix claim.

## Recommended next action

Run a bounded direct-evidence follow-up using two small real corpora, such as prose versus code or two curated text domains, with the same fixed-token ratio sweep and three seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-tiny data-mix ratio sweep
- Success threshold: A mixed ratio must improve aggregate worst-domain validation loss by at least 10% over both endpoint-only controls, with the best or near-best robust ratio recurring in at least two of three seeds.
- Stop condition: Stop if no mixed ratio beats both endpoints on worst-domain validation loss, or if all mixed-ratio gains are below 5% after three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/datamix-ratio-sweep-for-gpt-2-tiny-on-gb10-b9fd866c7633`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
