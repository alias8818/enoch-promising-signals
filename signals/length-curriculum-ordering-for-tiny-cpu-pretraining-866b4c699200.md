# Length-curriculum ordering for tiny CPU pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `length-curriculum-ordering-for-tiny-cpu-pretraining-866b4c699200`
Run ID: `length-curriculum-ordering-for-tiny-cpu-pretraining-866b4c699200-20260613T101558944319+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258851e1b744

## What looked useful

Short-to-long length ordering is a plausible stabilization/sample-efficiency mechanism for tiny pretraining, but the local evidence only supports a follow-up direct tiny-LM test. Long-to-short ordering appears harmful on this proxy.

## Boundaries and scale limits

The evidence is from a synthetic final-token memory task, not natural text; it uses a small recurrent model, not a transformer; random ordering also solved the toy task by 1000 updates; no large-scale or publication-grade language-model validation was run.

## Claim scope

In a bounded CPU-only synthetic pretraining proxy with a tiny NumPy RNN and variable lengths 8/16/32/64, short-to-long ordering slightly improved final loss and length-64 accuracy versus random ordering, while long-to-short ordering was substantially worse.

## Why it stopped

Proxy-only useful signal; not full validation and not paper-ready because the task is synthetic and random ordering also reaches near-ceiling performance.

## Recommended next action

Run a bounded token-budget-matched tiny transformer or GPT-style CPU/GPU pretraining follow-up on a real small text corpus, measuring validation perplexity by length bucket across at least 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Token-budget-matched tiny transformer length curriculum on real text
- Success threshold: Short-to-long improves final validation perplexity by at least 2% or reaches the same perplexity with at least 10% fewer tokens than random, without worse length-64 validation, in at least 2 of 3 seeds.
- Stop condition: Stop if short-to-long is within +/-1% of random on validation perplexity and convergence tokens across 3 seeds, or if it worsens long-bucket perplexity by more than 2%.

## Evidence references

- Artifact root: `<local-path>/projects/length-curriculum-ordering-for-tiny-cpu-pretraining-866b4c699200`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
