# INT4 Extreme Quantization with Residual Channel Preservation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `int4-extreme-quantization-with-residual-channel-preservation-9a88f9a4ed6d`
Run ID: `int4-extreme-quantization-with-residual-channel-preservation-9a88f9a4ed6d-20260614T020522825021+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fdc72ec0d6bc

## What looked useful

On GPT-2, plain INT4 increased NLL by 0.396339 over fp16. Preserving the top 5% activation-selected input channels reduced the NLL penalty to 0.190630, recovering about 51.9% of the plain INT4 loss at an estimated 4.811 bits/weight. Random 5% preservation recovered only 0.019587 NLL, suggesting activation-informed residual channel choice is the useful mechanism.

## Boundaries and scale limits

Only GPT-2 plus tiny smoke model; 16,384-token confirmation evaluation; dequantized quality probe rather than packed INT4 kernel; no latency, memory-bandwidth, training, or multi-model robustness evidence.

## Claim scope

Bounded post-training GPT-2 probe: preserving 1-5% activation-selected Conv1D input-channel rows in floating point while dequantizing the remaining weights from symmetric INT4 improves WikiText-2 subset perplexity versus plain INT4 and beats random preserved-channel controls at equal nominal overhead.

## Why it stopped

No-paper useful signal: the mechanism is supported in a bounded GPT-2 dequantized proxy, but paper-positive closure requires real packed-kernel storage/latency evidence and broader model/corpus validation.

## Recommended next action

Run a bounded deepen follow-up that implements packed INT4 plus fp16 residual-row inference and repeats the perplexity test on at least two additional 100M-500M parameter causal LMs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed INT4 residual-row inference across small causal LMs
- Success threshold: Activation-selected residual preservation at 2-5% rows recovers at least 30% of plain INT4 NLL degradation on at least two models, beats random controls by at least 0.05 NLL on each, and stays below 5 effective bits per weight.
- Stop condition: Stop if activation-selected residual rows fail to recover at least 10% of plain INT4 NLL degradation on the first additional model or do not beat random controls at equal overhead.

## Evidence references

- Artifact root: `<local-path>/projects/int4-extreme-quantization-with-residual-channel-preservation-9a88f9a4ed6d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
