# Domain mixture ratio sweep with tiny proxies

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `domain-mixture-ratio-sweep-with-tiny-proxies-880acfbc2433`
Run ID: `domain-mixture-ratio-sweep-with-tiny-proxies-880acfbc2433-20260629T205342054765+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a1bc16d9a396

## What looked useful

The tiny proxy selected the 0.75 Domain A ratio for a 75/25 target mixture, with bootstrap seed-resampling selecting 0.75 in 98.83% of samples. The 0.75 vs 0.5 margin was small at 0.0107 loss, but pure-domain mixtures were clearly rejected: pure B was 5.5291 target loss worse than best and pure A was 2.0852 worse.

## Boundaries and scale limits

Synthetic domains only; tiny model only; three seeds per ratio; no real corpora, tokenizer effects, curriculum effects, larger model scaling, or cross-scale transfer validation.

## Claim scope

Synthetic two-domain causal-language-model proxy with a 240,768-parameter Transformer, five Domain A train ratios, three seeds per ratio, 180 training steps per run, and a 75% Domain A / 25% Domain B target validation mixture.

## Why it stopped

Closed as no-paper useful signal: the evidence is synthetic proxy evidence, not direct validation for real domain-mixture selection.

## Recommended next action

Run a bounded real-text deepen test using the same ratio sweep on two small public domains and require proxy-selected ratios to improve held-out target mixture loss over pure-domain and 50/50 controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny proxy domain mixture sweep
- Success threshold: Proxy-selected target-neighborhood ratio beats pure-domain controls by at least 5% relative held-out target-mixture loss and beats 50/50 by a seed-stable margin whose bootstrap best-ratio probability is at least 0.90.
- Stop condition: Stop if the target-neighborhood ratio does not beat 50/50 or if ratio rankings are unstable across seeds with bootstrap best-ratio probability below 0.60.

## Evidence references

- Artifact root: `<local-path>/projects/domain-mixture-ratio-sweep-with-tiny-proxies-880acfbc2433`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
