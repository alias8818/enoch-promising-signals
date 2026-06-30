# Context-conditioned residual adapter for 2-bit draft speculation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `context-conditioned-residual-adapter-for-2-bit-draft-specu-c24784c5cd`
Run ID: `context-conditioned-residual-adapter-for-2-bit-draft-specu-c24784c5cd-20260523T121812790418+0000`

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

- Parent run decision: 2-bit Draft with Residual-Corrected Target Speculation: enoch://control-plane/projects/2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634/runs/2-bit-draft-with-residual-corrected-target-speculation-69d5b4ac9634-20260523T113045486686+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aaff3ccd450d

## What looked useful

True-context residual repair raised speculative distribution overlap from 0.038 to 0.352 and top-1 agreement from 0.081 to 0.323 on 923 held-out contexts; against a same-size shuffled-context control it added +0.123 overlap and +0.154 top-1 agreement.

## Boundaries and scale limits

The draft quantization covered only the LM head while hidden states came from the full-precision target; no full 2-bit transformer draft, real speculative decoding loop, latency/throughput measurement, multi-seed robustness, or larger-model validation was tested.

## Claim scope

On a Tier 1 small direct test using distilgpt2 hidden states and a rowwise 2-bit quantized output head, a rank-64 context-conditioned residual adapter improved held-out target/draft distribution overlap and top-1 agreement over raw 2-bit, context-free bias, and same-size shuffled-context controls.

## Why it stopped

Small direct mechanism support was achieved, but the evidence is not publication-grade because it repairs only a quantized LM head over full-precision hidden states.

## Recommended next action

Run a bounded deepen test on a fully 2-bit quantized tiny/GPT-2-small-class draft transformer with real speculative acceptance and throughput metrics before considering paper escalation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full 2-bit draft transformer residual adapter acceptance test
- Success threshold: At minimum, true-context residual adapter improves real speculative acceptance by at least 10 percent relative over the strongest 2-bit residual control without reducing measured decoding throughput by more than 5 percent.
- Stop condition: Stop as negative if the fully quantized draft shows less than 3 percent relative acceptance lift over the strongest control, or if adapter compute erases throughput gains despite improved logits.

## Evidence references

- Artifact root: `<local-path>/projects/context-conditioned-residual-adapter-for-2-bit-draft-specu-c24784c5cd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
