# Stochastic-Depth Volunteer Proof

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stochastic-depth-volunteer-proof-f98960146f3c`
Run ID: `stochastic-depth-volunteer-proof-f98960146f3c-20260607T073309412691+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74310f1de90c

## What looked useful

Stochastic-depth p=0.4 improved partial-depth accuracy by 0.0177 to 0.0346 absolute and accuracy retention by 0.304 to 0.597 versus dense across reduced-depth schedules, but reduced full-depth accuracy by 0.0427 absolute.

## Boundaries and scale limits

Synthetic task only; no real language corpus, GPT-2-small-class baseline, volunteer-network implementation, latency model, adversarial volunteer setting, or large-scale training was tested.

## Claim scope

On a 1.03M-parameter 6-layer synthetic language-model transformer, stochastic-depth training improved robustness and absolute accuracy when inference used only 2 to 4 active transformer blocks, compared with a parameter-matched dense control over 3 seeds.

## Why it stopped

Closed as no-paper useful signal because the mechanism worked in a synthetic proxy but had a substantial full-depth quality tradeoff and lacks direct real-corpus or volunteer-systems evidence.

## Recommended next action

Run a bounded deepen follow-up on a real small language-modeling corpus with GPT-2-small-class or parameter-matched toy baselines, requiring partial-depth robustness without more than a small full-depth quality loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Corpus Partial-Depth Robustness for Stochastic-Depth Transformers
- Success threshold: Stochastic-depth model beats dense by at least 0.15 retention at 50% active layers and has no more than 10% worse full-depth validation loss across seeds.
- Stop condition: Stop if stochastic-depth either fails to improve 50% active-layer retention by 0.10 or worsens full-depth validation loss by more than 20% after matched training.

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-depth-volunteer-proof-f98960146f3c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
