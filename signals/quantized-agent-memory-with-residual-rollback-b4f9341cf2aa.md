# Quantized Agent Memory with Residual Rollback

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-agent-memory-with-residual-rollback-b4f9341cf2aa`
Run ID: `quantized-agent-memory-with-residual-rollback-b4f9341cf2aa-20260530T061340963790+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/dc7e51af54d2

## What looked useful

Residual rollback is useful as a verified-miss repair mechanism, not as a universal cache. In close-cluster stress tests, 2-bit quantized recall was 0.6837 and feedback-enabled rollback reached 1.000, while cached-only recall improved to 0.7850-0.8200 under Zipfian access but fell below quantized-only under uniform access.

## Boundaries and scale limits

No real agent, language model, learned memory writer, or non-oracle verifier was tested. Runs used up to 8192 memories, 128 dimensions, 5000 queries per trial, and synthetic clustered vectors on one CPU worker.

## Claim scope

Synthetic vector associative-memory benchmark: 2-bit quantized memory with feedback-enabled residual rollback can repair retrieval misses when the true memory remains in the quantized top-32 candidate set; cached residuals improve future recall only under repeated Zipfian access.

## Why it stopped

No-paper closure: evidence is synthetic and mixed, with strong dependence on feedback-enabled top-R rollback rather than a validated practical agent-memory loop.

## Recommended next action

Stop this run as a synthetic useful signal; next test should replace oracle rollback with a concrete verifier in a real agent memory task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Verifier-Gated Residual Rollback in a Real Agent Memory Task
- Success threshold: At 2-bit or 3-bit memory, verifier-gated rollback recovers at least 50% of the downstream success loss from quantization while retaining at least 4x memory compression versus fp32 and adding less than 20% retrieval latency.
- Stop condition: Stop if verifier-triggered rollback recovers less than 25% of quantization-induced downstream loss or if verifier errors erase the recall gains on two independent tasks.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-agent-memory-with-residual-rollback-b4f9341cf2aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
