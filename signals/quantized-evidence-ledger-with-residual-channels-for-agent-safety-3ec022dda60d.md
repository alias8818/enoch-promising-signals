# Quantized Evidence Ledger with Residual Channels for Agent Safety

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-evidence-ledger-with-residual-channels-for-agent-safety-3ec022dda60d`
Run ID: `quantized-evidence-ledger-with-residual-channels-for-agent-safety-3ec022dda60d-20260522T152004560099+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bd4403e6afb2

## What looked useful

At 18.75% of full 32-bit storage, 2-bit salience residual-8 improved AUPRC from 0.5698 for quantized-only and 0.5841 for random residual-8 to 0.6496, reduced FPR@95TPR from 0.6242/0.6175 to 0.5383, and recovered audit recall from 0.0318/0.1261 to 0.8318. At 15.625% storage, 1-bit salience residual-8 improved AUPRC from 0.4428 and 0.4679 to 0.5676 and audit recall from 0.0 and 0.1136 to 0.8281. 3-bit quantization alone matched full exact performance, limiting generality.

## Boundaries and scale limits

Synthetic traces only; 10 seeds; no real agent logs, no LLM/tool-use traces, no online residual router, no adversarial/tamper tests, and no production latency or storage-system validation. A 3-bit quantized ledger already preserved critical counts in this toy distribution, so the mechanism is useful only under sufficiently aggressive or poorly scaled quantization.

## Claim scope

In a synthetic count-vector agent-evidence proxy with rare safety-critical evidence and a shared 1-2 bit quantized ledger, exact salience-selected residual channels recover erased critical evidence and improve classifier/audit metrics over quantized-only and random-residual controls at matched storage budgets.

## Why it stopped

Bounded synthetic evidence supports a mechanism under harsh quantization but is proxy-only and mixed; it is not a full validation or paper-positive result.

## Recommended next action

Stop this run as no-paper useful signal; next run should test a non-oracle residual router on semi-realistic agent/tool traces with matched-storage baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Non-oracle residual routing on semi-realistic agent evidence traces
- Success threshold: At a fixed storage budget under 20% of full 32-bit exact ledger size, a non-oracle residual router recovers at least 70% of the oracle residual AUPRC gain over quantized-only and achieves at least 0.65 audit recall on critical evidence, outperforming random residual controls across at least 5 seeds or splits.
- Stop condition: Stop if non-oracle routing fails to beat random residual controls by at least 0.03 AUPRC or 0.20 audit recall at matched storage on two independently generated or collected trace sets.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-evidence-ledger-with-residual-channels-for-agent-safety-3ec022dda60d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
