# Sub-4-bit Activation Quantization with Outlier Residual Routing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sub-4-bit-activation-quantization-with-outlier-residual-routing-d6b061ec243c`
Run ID: `sub-4-bit-activation-quantization-with-outlier-residual-routing-d6b061ec243c-20260620T075637537641+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a258cba71a72

## What looked useful

3-bit activation quantization plus sparse outlier residual routing gave a reproducible reconstruction improvement on two GPT-family models: 3-bit + 1% residual achieved 0.533x distilgpt2 and 0.657x GPT-2 small relative MSE versus plain 4-bit, while 2-bit + 2% residual stayed 2.61x and 3.87x worse than plain 4-bit.

## Boundaries and scale limits

Reconstruction-only benchmark on 8 short prompts; no end-to-end perplexity, no production packed metadata, no custom kernel, no latency or bandwidth measurement, no larger model validation.

## Claim scope

On distilgpt2 and GPT-2 small MLP projection activation traces, groupwise 3-bit quantization with a sparse exact residual route for about 0.5-1.0% of largest-magnitude elements can match or beat plain 4-bit reconstruction relative MSE; 2-bit with up to 2% residual remains worse than plain 4-bit.

## Why it stopped

The result is a bounded reconstruction mechanism signal, not a full validation; it lacks end-to-end quality and systems evidence required for a paper-ready claim.

## Recommended next action

Stop this worker run as no-paper useful signal; next run should test 3-bit sparse residual activation quantization in an end-to-end GPT-2 small perplexity and packed-metadata benchmark against plain 4-bit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end GPT-2 small 3-bit activation residual routing benchmark
- Success threshold: 3-bit plus residual must match or improve plain 4-bit perplexity within 1% relative while showing lower packed activation payload or measured memory traffic after residual metadata accounting.
- Stop condition: Stop if metadata overhead brings effective storage above plain 4-bit with mask/indices included, or if perplexity is more than 1% worse than plain 4-bit after tuning residual fraction up to 1%.

## Evidence references

- Artifact root: `<local-path>/projects/sub-4-bit-activation-quantization-with-outlier-residual-routing-d6b061ec243c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
