# Actual local-LLM cascade routing on held-out answer-keyed QA

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `actual-local-llm-cascade-routing-on-held-out-answer-keyed-19a86b5b3d`
Run ID: `actual-local-llm-cascade-routing-on-held-out-answer-keyed-19a86b5b3d-20260619T065052409667+0000`

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

- Parent run decision: CPU cascade router: difficulty-based dispatch across tiny/medium local models: enoch://control-plane/projects/cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526/runs/cpu-cascade-router-difficulty-based-dispatch-across-tiny-medium-local-models-49b394806526-20260619T053942292708+0000
- Parent run decision: Direct local-model cascade routing on answer-keyed natural-language tasks: enoch://control-plane/projects/direct-local-model-cascade-routing-on-answer-keyed-natural-789a8de569/runs/direct-local-model-cascade-routing-on-answer-keyed-natural-789a8de569-20260619T055658350358+0000

## What looked useful

Cascade routing had held-out F1 0.5679 at 35.7% large-call rate versus small-only F1 0.4174, random same-budget F1 0.5515, inverted same-budget F1 0.4353, and large-only F1 0.6659. The confidence signal is real but too weak and overconfident on grounded wrong spans.

## Boundaries and scale limits

28 held-out examples after 12-example calibration; CPU-only sequential llama.cpp subprocess inference; heuristic confidence only; small Qwen tiers only; not a production serving or broad benchmark validation.

## Claim scope

On a fixed-seed 40-example SQuAD v1.1 dev sample using local Qwen2.5 0.5B and 1.5B GGUF models, a heuristic cheap-tier confidence cascade improved over small-only and inverted/random same-budget controls but did not match the large-only baseline.

## Why it stopped

No-paper mixed result: direct local-LLM evidence supports a weak routing mechanism, but the tested heuristic cascade underperformed the real large-only baseline and only narrowly exceeded random same-budget F1.

## Recommended next action

Run a bounded deepen follow-up with a learned or logprob-calibrated router on 100-300 fixed-seed held-out QA examples and require improvement over both random same-budget routing and the large-only cost-quality curve.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned confidence routing for local-LLM held-out QA cascades
- Success threshold: On held-out QA, learned routing must improve at least 0.05 F1 over random same-budget routing and be within 0.03 F1 of large-only while reducing large calls by at least 40%.
- Stop condition: Stop if calibrated routing fails to beat random same-budget F1 by 0.03 or if high-confidence wrong-span errors remain above 20% of accepted small answers.

## Evidence references

- Artifact root: `<local-path>/projects/actual-local-llm-cascade-routing-on-held-out-answer-keyed-19a86b5b3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
