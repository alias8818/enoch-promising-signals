# Curriculum vs Shuffled Ordering for GPT-2-Small Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `curriculum-vs-shuffled-ordering-for-gpt-2-small-pretraining-6a8f34b043c1`
Run ID: `curriculum-vs-shuffled-ordering-for-gpt-2-small-pretraining-6a8f34b043c1-20260629T163951467469+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/feaa187561ee

## What looked useful

Strict sorted curriculum appears to reweight learning toward late hard examples rather than improve the full distribution: aggregate validation loss was 3.9146 for curriculum versus 2.3950 for shuffled, but hardest-level loss was 4.1831 for curriculum versus 4.4053 for shuffled.

## Boundaries and scale limits

Synthetic multilevel sequence corpus, small 4-layer 128-dim Transformer, 3 seeds, 3 epochs, short fixed-budget run; not a GPT-2-small 124M-parameter real-corpus pretraining validation.

## Claim scope

In a bounded synthetic causal-LM probe using the same corpus and token budget, strict easy-to-hard ordering underperformed global shuffling on aggregate held-out next-token loss across three seeds, while improving the hardest synthetic level.

## Why it stopped

Proxy/early falsification of strict easy-to-hard curriculum as an aggregate improvement; evidence is direct for a synthetic causal-LM setup but not full GPT-2-small pretraining.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should compare shuffled against a paced curriculum with mixed review on the same synthetic setup before any real-text GPT-2-small-class run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Paced Curriculum With Mixed Review for Causal-LM Pretraining
- Success threshold: Mixed-review curriculum must beat shuffled aggregate validation loss by at least 0.05 nats/token while not worsening any level by more than 0.05 nats/token across seeds.
- Stop condition: Stop if mixed-review curriculum fails to beat shuffled aggregate validation loss on the synthetic setup or only shifts loss from easy levels to hard levels.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-vs-shuffled-ordering-for-gpt-2-small-pretraining-6a8f34b043c1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
