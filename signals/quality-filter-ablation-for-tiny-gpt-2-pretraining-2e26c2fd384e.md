# Quality-filter ablation for tiny GPT-2 pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quality-filter-ablation-for-tiny-gpt-2-pretraining-2e26c2fd384e`
Run ID: `quality-filter-ablation-for-tiny-gpt-2-pretraining-2e26c2fd384e-20260621T043056640426+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3adb369ee78e

## What looked useful

Across three seeds, quality filtering reduced clean validation loss by 0.1590 nats vs unfiltered and 0.1592 nats vs random-same-size control, while increasing noisy validation loss by 1.4066 and 1.3745 nats respectively.

## Boundaries and scale limits

Synthetic token corpus, deliberately matched quality heuristic, 2-layer 128-hidden GPT-2-style model, 400 optimizer steps per arm, three seeds. Not direct evidence for real web text, GPT-2-small-class scale, long pretraining, or downstream transfer.

## Claim scope

In a controlled synthetic tiny GPT-2-style causal-LM pretraining proxy, a quality filter that removes corrupted sequences improves clean held-out validation loss under a fixed training-token budget, but substantially worsens noisy held-out validation loss.

## Why it stopped

Proxy evidence supports a mechanism but is not direct/full validation; the result is synthetic and therefore insufficient for publication-grade GPT-2 pretraining claims.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded real-text three-arm ablation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text tiny GPT-2 quality-filter ablation
- Success threshold: Quality-filtered clean validation perplexity improves by at least 3% versus both controls across seeds, while broad/noisy validation perplexity degrades by less than 5%.
- Stop condition: Stop if the filtered arm does not beat both controls on clean validation loss in at least two of three seeds, or if broad/noisy validation degradation exceeds 5%.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filter-ablation-for-tiny-gpt-2-pretraining-2e26c2fd384e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
